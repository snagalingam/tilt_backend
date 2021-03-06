import csv
import json
import os
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
SCRIPT_DIR = os.path.dirname(__file__)

################################################################################
# This function extracts the data from a scholarship page
################################################################################
def extract_data(url):
    response = requests.get(url, headers=HEADERS)
    page = BeautifulSoup(response.text, 'html.parser')
    # use selineum to click link
    name = page.find('h1').text
    award_info = page.find_all("div", {"class": "award-info-row"})[0].contents
    ammont = None
    deadline = None
    available = None

    for each in award_info:
        if each != '\n':
            text = each.text.strip('\r\n').strip()
            if "$" in text or "Amount" in text:
                amount = text
            elif "," in text or "Deadline" in text:
                deadline = text
            elif "Awards Available:" in text:
                right_index = text.rindex("  ")
                available = text[right_index + 1:]

    description = page.find('li', { "class": "scholdescrip" }).text.replace("ADVERTISEMENT", "").strip('\r\n')
    body = page.find('ul', { "id": "ulScholDetails" })
    start_contact = False
    count = 1
    contact_name = None
    contact_address = None
    contact_city = None
    contact_state = None
    contact_zipcode = None
    contact_email = None
    contact_phone = None
    contact_ext = None

    for each in body:
        if each != '\n':
            if each.text.strip() == "Contact":
                start_contact = True
                continue

            if start_contact:
                info = each.text.strip('\r\n').strip()
                if count == 1:
                    contact_name = info
                    count += 1
                elif count == 2:
                    contact_address = info
                    count += 1
                elif count == 3:
                    try:
                        comma = info.index(",")
                        left = info.index(" ")
                        right = info.rindex(" ")
                        contact_city = info[0:comma]
                        contact_zipcode = info[right + 1:]
                        contact_state = info[left:right].replace(contact_city, "").strip()[-2:]
                        count += 1
                    except:
                        contact_address + " " + info

                elif "@" in info:
                    contact_email = info
                elif any(char.isdigit() for char in info):
                    if "tel:" in info:
                        contact_phone = info
                    elif "ext:" in info:
                        contact_ext = info
                    elif "fax:" in info:
                        continue
                    else:
                        contact_phone = info

    data = {
        "Name": name,
        "Amount": amount,
        "Deadline": deadline,
        "Available": available,
        "Description": description,
        "Provider": contact_name,
        "Address": contact_address,
        "City": contact_city,
        "State": contact_state,
        "Zipcode": contact_zipcode,
        "Email": contact_email,
        "Phone": contact_phone,
        "Ext": contact_ext,
    }

    return data


################################################################################
# This function gets the scholarship pages based on monthly deadlines
################################################################################
def get_scholarships_based_on_deadline(month):
    url = f"https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/deadline"
    response = requests.get(url, headers=HEADERS)
    page = BeautifulSoup(response.text, 'html.parser')
    links = page.find_all("ul", {"id": "ullist"})
    urls = links[0].find_all("a")
    scholarship_urls = {}

    print("Status Update -> Getting Scholarships")

    for url in urls:
        name = url.text
        href = url.get("href")
        root = "https://www.scholarships.com"
        scholarship_urls[name] = root + href

    entire_list = {}
    count = 0
    for name, url in scholarship_urls.items():
        if month in name:
            response = requests.get(url + "?sortOrder=duedate&sortDirection=asc", headers=HEADERS)
            page = BeautifulSoup(response.text, 'html.parser')
            table = page.find_all("table", {"class": "scholarshiplistdirectory"})
            urls = table[0].find_all("a")
            scholarship_urls = {}

            for url in urls[3:]:
                print(f"Status Update -> Getting Scholarship {count}")
                count += 1

                contact = url.text
                href = url.get("href")
                root = "https://www.scholarships.com"
                scholarship_urls[contact] = root + href
                data = extract_data(root + href)

                with open(os.path.join(SCRIPT_DIR, 'scholarship_data.json'), '+a') as f:
                    d = json.dumps(data, indent=2, ensure_ascii=False)
                    f.write(d + ',')

            entire_list[name] = scholarship_urls
            with open(os.path.join(SCRIPT_DIR, 'entire_list.json'), '+a') as f:
                data = json.dumps(entire_list, indent=2, ensure_ascii=False)
                f.write(data)


################################################################################
# Convert scholarship json file to csv file
################################################################################
def make_csvs(json_file):
    json_data = json.load(open(f'{json_file}.json'))
    count = 1
    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    for month in months:
        with open(f'{month}.csv', 'w') as f:
            headers = [
                "Url",
                "Name",
                "Amount",
                "Deadline",
                "Available",
                "Description",
                "Provider",
                "Address",
                "City",
                "State",
                "Zipcode",
                "Email",
                "Phone",
                "Ext",
                "Website"]
            csv_writer = csv.writer(f)
            csv_writer.writerow(headers)

        for data in json_data:
            if month in data["Deadline"]:

                url = data["Url"]
                name = data["Name"]
                amount = data["Amount"]
                deadline = data["Deadline"]
                available = data["Available"]
                description = data["Description"]
                contact_name = data["Provider"]
                contact_address = data["Address"]
                contact_city = data["City"]
                contact_state = data["State"]
                contact_zipcode = data["Zipcode"]
                contact_email = data["Email"]
                contact_phone = data["Phone"]
                contact_ext = data["Ext"]
                website = data["Website"]

                each_line = (
                    url,
                    name,
                    amount,
                    deadline,
                    available,
                    description,
                    contact_name,
                    contact_address,
                    contact_city,
                    contact_state,
                    contact_zipcode,
                    contact_email,
                    contact_phone,
                    contact_ext,
                    website
                    )

                with open(f'{month}.csv', '+a') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(each_line)

                return print(f'{json_file}.json converted to csv file.')


################################################################################
# This function gets the apply links
################################################################################
FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# json file of all scholarships from deadline table
#scholarships = json.load(open(f"{FOLDER_PATH}/csvs/entire_url_list.json"))
# json file of all deails from scholarships
#data = json.load(open(f"{FOLDER_PATH}/csvs/scholarship_data.json"))

def get_apply_link(scholarships, data):
    count = 0
    options = Options()

    # invisibility option for browser
    # options.add_argument("--headless")

    chromedriver = "/Users/pd/Desktop/Projects/scrapper/tilt_scripts/common_ds/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)

    # resize browser window (width, height) min_width=1000 or login will not be visible
    driver.set_window_size(1000, 100)
    driver.set_window_position(0, 0)

    for month in scholarships.keys():
        for url in scholarships[month].values():

            # find login and click on first open
            if count == 0:
                driver.get(f"https://www.scholarships.com/")
                login = driver.find_element_by_link_text("Login")
                login.click()

                # input email and password and submit
                email = driver.find_element_by_css_selector("input[type=email")
                email.send_keys("tiltaccess@gmail.com")
                password = driver.find_element_by_css_selector("input[type=password")
                password.send_keys("tilt1234")
                password.send_keys(Keys.RETURN)

            # go to scholarship url
            try:
                driver.get(url)
                apply = driver.find_element_by_id("apply-now-button")
                href = apply.get_attribute("href")
                start = href.index("http")
                end = href.index("',")
                scholarship_url = href[start:end]

                # add scholarship_url to data
                data[count]["scholarship_url"] = scholarship_url

                # with open(f'new_data.json', '+a') as f:
                #     d = json.dumps(data[count], indent=2, ensure_ascii=False)
                #     f.write(d + ',')

                # print(f" ======> COUNT {count} : {scholarship_url}")

            except:
                pass

            count += 1

    # closer browser when done
    return driver.close()


################################################################################
# Run these functions
################################################################################
get_scholarships_based_on_deadline(month="March")
