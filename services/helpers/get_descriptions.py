import requests
from bs4 import BeautifulSoup
import json
import time
from pprint import pprint
from itertools import islice

# ---------- Get description from meta tag -------------------

def get_description(file):

    source = json.load(open(f'{file}.json'))
    collection = []
    count = 0

    for college in source:
        url = college['fields'].get('website')
        count += 1
        print(f' count ===> : {count}')

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            metas = soup.find_all('meta')

            for meta in metas:
                if 'name' in meta.attrs:
                    if meta.attrs['name'] == "Description" or meta.attrs['name'] == "description":
                        if 'content' in meta.attrs:
                            description = meta.attrs["content"]

                            college['fields']['description'] = description
                            collection.append(college)

        except:
            college['fields']['description'] = ""
            collection.append(college)
            pass

    with open('collection.json', 'w') as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)
    print('collection done')
    print('done')


# get_description('website_list')

# ---------- Get description from meta tag -------------------

def add_blank_description(file):

    source = json.load(open(f'{file}.json'))
    collection = []
    count = 0

    for college in source:
        description = college['fields'].get('description', '')
        # breakpoint()
        count += 1
        print(f' count ===> : {count}')
        college['pk'] = count
        college['fields']['description'] = description
        college['fields']['popularity_score'] = 0
        collection.append(college)

    with open('collection1.json', 'w') as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)
    print('collection1 done')
    print('done')


# add_blank_description('collection')


# ---------- Compare descriptions -------------------

def compare_descriptions(source, target):

    source_file = json.load(open(f'{source}.json'))
    target_file = json.load(open(f'{target}.json'))
    collection = []
    count = 0

    for college in source_file:
        count += 1
        print(f' count ===> : {count}')

        for each in target_file:
            source_name = college['fields']['name']
            target_name = each['fields']['name']
            target_description = each['fields'].get('description', '')

            if source_name == target_name:
                college['fields']['description'] = target_description

        collection.append(college)
        # breakpoint()

    with open('collection2.json', 'w') as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)
    print('collection1 done')
    print('done')


# compare_descriptions('collection1', 'collection')
