from google.google_places import extract_photo_urls, GooglePlacesAPI
from fav_finder import get_favicon
import csv
import json
import time
from pprint import pprint
from itertools import islice

#---------------------------  CREATE JSON LIST  ---------------------------

def create_list_json(source, target):
    limit = 0
    stop = 1

    with open(f'{source}.csv', 'r') as c_f:
        csv_reader = csv.reader(c_f)
        _list = []

        for line in csv_reader:
            # target values
            unit_id = line[0]
            _list.append(unit_id)

            limit += 1
            print(limit)
            # if limit == stop:
            #     break

            # with open(f'{target}.json', 'w') as new_file:
            #     data = json.dumps(_list, indent=2)
            #     new_file.write(data)

    return print(f'''

    {target}.json => CREATED

    ''')

# source file
# create_list_json('colleges_zero_results', 'unit_id')

#---------------------------  FILTER MODIFY CSV  ---------------------------

def make_modified_csv(source, target, check):
    json_data = json.load(open(f'{check}.json'))

    with open(f'{source}.csv', 'r') as c_f:
        csv_reader = csv.reader(c_f)
        limit = 0
        stop = 5

        with open(f'{target}.csv', 'w') as f:
            csv_writer = csv.writer(f)

            for line in csv_reader:
                unit_id = line[0]
                ope_id = line[1]
                name = line[3]
                city = line[4].lower()
                zipcode = line[6]
                each_line = (unit_id, ope_id, name, city, zipcode)
                # print(each_line)

                # conditional modifications
                if unit_id in json_data:
                    csv_writer.writerow(each_line)
                    limit += 1
                    print(limit)
                # if limit == stop:
                #     break

        return print(f'''

        {limit} colleges found

        ''')

# (source, new_file) => creates new modified csv file
# make_modified_csv('csv_files/original_data', 'csv_files/google_zero', 'unit_id')

#---------------------------  CREATE JSON LIST OF COLLEGE SEED ---------------------------

def check_colleges_data(action, key):

    limit = 0
    nums = 0
    _list = []
    count = 0

    while True:
        if limit == 24:
            break
        elif limit < 10:
            nums = f"0{limit}"
        else:
            nums = f"{limit}"

        json_data = json.load(open(f'colleges_seed_{nums}.json'))
        limit += 1

        # action condition
        if action == 'count':
            file_length = len(json_data)
            count += file_length

        elif action == 'list':
            for each in json_data:
                _list.append(each[key])

    # action result
    if action == 'count':
        return print(count)

    elif action == 'list':
        # with open(f'list_of_{key}s.json', 'w') as f:
        #     data = json.dumps(_list, indent=2)
        #     f.write(data)
        return print(f'''

        list_of_{key}s.json => CREATED

        ''')

#---------------------------  CREATE JSON LIST OF SINGLE FILE ---------------------------

def check_single_file(source, target, key):
    _list = []
    ids = []
    limit = 0
    json_source = json.load(open(f'{source}.json'))
    json_target = json.load(open(f'{target}.json'))

    for each in json_target:
        if each[key] in json_source:
            limit += 1
            print(limit)
            _list.append(each)

    # print(ids)

    # with open(f'check_{key}s.json', 'w') as f:
    #     data = json.dumps(_list, indent=2)
    #     f.write(data)

    return print(f'''

        check_{key}s.json => CREATED

        ''')

# check_single_file('unit_id', 'csv_files/colleges_infos', 'unit_id')

#---------------------------  CREATE NOT INCLUDED LIST ---------------------------

def not_included_list(source, check, key='unit_id'):

    json_list = json.load(open(f'{source}.json'))
    counter = 0

    with open(f'{check}.csv', 'r') as c_f:
        csv_reader = csv.reader(c_f)

    for line in csv_reader:
        counter += 1

        unit_id = line[0]
        if unit_id in json_list:
            counter += 1

            with open('list_of_forgotten.csv', 'a') as new_file:
                    csv_writer = csv.writer(new_file)
                    csv_writer.writerow(line)

    return print(f'''

            list_of_forgotten.csv => CREATED

            ''')

#---------------------------  CONVERT CSV DATA TO JSON DATA ---------------------------

def convert_to_json(csv_file):
    counter = 0
    arr = []
    with open(f'{csv_file}.csv', 'r') as c_f:
        csv_reader = csv.reader(c_f)

        for line in csv_reader:
            unit_id = line[0]
            ope_id = line[1]
            name = line[2]
            city = line[3]
            zipcode = line[4]

            each = {
                "unit_id": unit_id,
                "ope_id": ope_id,
                "name": name,
                "city": city,
                "zipcode": zipcode
            }

            arr.append(each)
            counter += 1
            print(counter)
                # print(each)

        # with open(f'{csv_file}s.json', 'w') as f:
        #     data = json.dumps(arr, indent=2)
        #     f.write(data)


# convert_to_json('csv_files/colleges_info')

#---------------------------  GOOGLE PLACE API  ---------------------------

def get_google_info(file_name, location):
    scorcards = []
    limit = 25
    step = None
    stop = None
    start = 0
    nums = 0

    while True:

        if limit < 10:
            nums = f"0{limit}"
        else:
            nums = f"{limit}"

        print(f"LIMIT: => {limit}")
        with open(f'{file_name}.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # islice(argument, start, stop, step)
                # islice('ABCDEFG', 2) --> A B
                # islice('ABCDEFG', 2, 4) --> C D
                # islice('ABCDEFG', 2, None) --> C D E F G
                # islice('ABCDEFG', 0, None, 2) --> A C E G

            # 6807 total colleges
            for line in islice(csv_reader, start, stop, step):
                unit_id = line[0]
                ope_id = line[1]
                name = line[2]
                city = line[3]
                zipcode = line[4]

                api = GooglePlacesAPI()
                # time.sleep(.5) # slows down the api in seconds

                if location == 'city':
                    print('''-----[current]-----: =>''', name, city)
                    data = api.details(name, city)
                elif location == 'zipcode':
                    print('''-----[current]-----: =>''', name, zipcode)
                    data = api.details(name, zipcode)

                # if google api result is zero print to colleges_zero_results.csv
                if data is None:
                    with open('colleges_zero_results.csv', 'a') as new_file:
                        csv_writer = csv.writer(new_file)
                        each_line = (unit_id, ope_id, name, city, zipcode)
                        csv_writer.writerow(each_line)

                    # if google api result is zero pass
                try:

                    try:
                        photos_result = data["result"]["photos"]
                        photos = extract_photo_urls(photos_result)
                        main_photo = photos[0]
                    except:
                        photos = []
                        main_photo = ''

                    website = data["result"].get("website", '')
                    favicon = get_favicon(website)
                    place_id = data["place_id"]
                    business_status = data["result"].get("business_status", '')
                    name = data["result"]["name"]
                    lat = data["result"]["geometry"]["location"]["lat"]
                    lng = data["result"]["geometry"]["location"]["lng"]
                    address = data["result"]["formatted_address"]
                    phone_number = data["result"].get(
                        "formatted_phone_number", '')
                    url = data["result"]["url"]
                    types = data["result"]["types"]
                    scorcard = {
                        "unit_id": unit_id,
                        "ope_id": ope_id,
                        "place_id": place_id,
                        "business_status": business_status,
                        "name": name,
                        "address": address,
                        "phone_number": phone_number,
                        "lat": lat,
                        "lng": lng,
                        "url": url,
                        "website": website,
                        "favicon": favicon,
                        "main_photo": main_photo,
                        "photos": photos,
                        "types": types
                    }
                    scorcards.append(scorcard)

                    # increment num
                    # with open(f'colleges_seed_{nums}.json', 'w') as new_file:
                    #         data = json.dumps(scorcards, indent=2)
                    #         new_file.write(data)

                except:
                    print(f'FAILED => {data}')
                    pass

            if limit == 25:
                break
            else:
                # start = stop
                # stop += 318
                limit += 1
                scorcards = []

        return print(f'''

            get_google_info => DONE

        ''')


# get_google_info('csv_files/google_zero', 'city')
