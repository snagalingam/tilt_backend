import re
import bs4
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# json file of all scholarships from deadline table
scholarships = json.load(open(f"{FOLDER_PATH}/csvs/entire_url_list.json"))
# json file of all deails from scholarships
data = json.load(open(f"{FOLDER_PATH}/csvs/scholarship_data.json"))

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
                apply.click()

                # switch to popup window         
                driver.switch_to.window(driver.window_handles[-1])
                driver.set_window_size(100, 100)
                driver.set_window_position(0, 0)
                scholarship_url = driver.current_url
                title = driver.title

                # add scholarship_url to data 
                data[count]["scholarship_url"] = scholarship_url
                data[count]["organization"] = title

                with open(f'new_data.json', '+a') as f:
                    d = json.dumps(data[count], indent=2, ensure_ascii=False)
                    f.write(d + ',')

                print(f" ======> COUNT {count} : {title}")
                            # close popup
                time.sleep(3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                breakpoint()
            
            count += 1

    # closer browser when done
    driver.close()
