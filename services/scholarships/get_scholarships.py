import requests
from bs4 import BeautifulSoup
import csv
import json
import re
from io import StringIO

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

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
        "Contact": contact_name, 
        "Address": contact_address, 
        "City": contact_city, 
        "State": contact_state, 
        "Zipcode": contact_zipcode, 
        "Email": contact_email, 
        "Phone": contact_phone, 
        "Ext": contact_ext, 
    }

    return data

def get_scholarship_table(url_list):
    entire_list = {}
    count = 1
    month = 0
    for name, url in url_list.items():
        month += 1
        # sort by earliest deadline
        if month >= 5:
            response = requests.get(url + "?sortOrder=duedate&sortDirection=asc", headers=HEADERS)
            page = BeautifulSoup(response.text, 'html.parser')
            table = page.find_all(
                "table", {"class": "scholarshiplistdirectory"})

            # create csv file for tables
            # with open(f"{name}.csv", "wt") as f:
            #     f.write(table[0].text)

            urls = table[0].find_all("a")
            scholarship_urls = {}

            for url in urls[3:]:
                contact = url.text
                href = url.get("href")
                root = "https://www.scholarships.com"
                scholarship_urls[contact] = root + href

                # extract data from url 
                # data = extract_data(root + href)
                # create json file for each scholarship
                # with open(f'scholarship_data.json', '+a') as f:
                #     d = json.dumps(data, indent=2, ensure_ascii=False)
                #     f.write(d + ',')

                print(f' COUNT ===> : {count}')
                count += 1

            entire_list[name] = scholarship_urls
            # create json file for entire_list
            # with open(f'entire_list.json', '+a') as f:
            #     data = json.dumps(entire_list, indent=2, ensure_ascii=False)
            #     f.write(data)

    return entire_list

def get_scholarship_urls():
    url = f"https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/deadline"
    response = requests.get(url, headers=HEADERS)
    page = BeautifulSoup(response.text, 'html.parser')
    links = page.find_all(
        "ul", {"id": "ullist"})
    urls = links[0].find_all("a")
    scholarship_urls = {}

    for url in urls:
        name = url.text
        href = url.get("href")
        root = "https://www.scholarships.com"
        scholarship_urls[name] = root + href

    return get_scholarship_table(scholarship_urls)

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
                "Contact",
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
                contact_name = data["Contact"]
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

                # with open(f'{month}.csv', '+a') as f:
                #     csv_writer = csv.writer(f)
                #     csv_writer.writerow(each_line)
                # print(f' COUNT ===> : {count}')
                count += 1

                return print(f'{json_file}.json converted to csv file.')
