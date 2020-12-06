import re
import bs4
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

def get_common_ds(college_names):
    count = 0
    options = Options()
    data_dir = "<path to store downloaded pdf>"

    # invisibility option for browser (however, files with the same name will be replaced: use window resizing instead)
    # options.add_argument("--headless")

    # download automatically on cilck option
    options.add_experimental_option('prefs',  {
        "download.default_directory": data_dir,
        "plugins.always_open_pdf_externally": True
        }
    )

    # https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
    chromedriver = "<path to webdriver>"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    
    # resize browser window (width, height)
    driver.set_window_size(100, 100)
    driver.set_window_position(0, 0)

    for c in college_names[count:]:
        name = c["name"]
        website = c["website"]
        # name cuts off at ampersand (&) for google search
        # remove ampersand (&) from name and search name without it
        if "&" in name:
            index = name.index("&")
            front = name[0:9]
            back = name[10:]
            name = f'{front}{back}'
        # print(name)
        # print(website)

        driver.get(f'https://www.google.com/search?q=filetype:pdf+common+data+set+2019-2020+{name}&start=0')

        try:
            # targets first link in google search
            result = driver.find_element_by_tag_name("h3")
            words = ["CDS", "cds", "Cds", "Common", "COMMON"]
            skip = False

            for word in words:
                # match h3 text to words list
                if word in result.text:
                    result.click()
                    skip = True
                    # slows script down otherwise ip flagged for unusual behavior
                    time.sleep(5)

            # if no match then link click skipped
            if not skip:
                # slows script down otherwise ip flagged for unusual behavior
                time.sleep(3) 
                skip = False
        except:
            pass

        print(f' ======> COUNT {count}')
        count += 1

    # closes browser
    driver.close()

# college_names = json.load(open(f'college_names.json'))
# get_common_ds(college_names)
# print(ROOT_PATH)