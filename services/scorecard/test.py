def find_all_and_missing_pks():
    pks = []
    missing_pks = []

    with open("../../fixtures/colleges_seeds.json") as file:
        data = json.load(file)

        for item in data:
            pk = item['pk']
            pks.append(pk)

    pks.sort()

    for num in range(pks[0], pks[-1]+1):
        if num not in data:
            missing_pks.append(num)

    with open('all_pks.json', 'w') as outfile:
        json.dump(pks, outfile, indent=4, sort_keys=True)

    with open('missing_pks.json', 'w') as outfile:
         json.dump(missing_pks, outfile, indent=4, sort_keys=True)


def find_max_pk_college_keys():
    max_pk = 0
    counter = 0

    with open("college_keys.json") as file:
        data = json.load(file)

    for item in data:
        for key, value in item.items():
            pk = value['pk']
            if max_pk < pk:
                max_pk = pk

    return(max_pk)


def add_new_scorecard_unit_ids_to_colleges_keys():
    current_ids = []
    missing_ids = []

    with open('scorecard_unit_ids.json') as file:
        scorecard = json.load(file)

    with open('college_keys.json') as file:
        college_keys = json.load(file)

    for item in current_ids:
        id = item['id']

        try:
            college_keys[id]
            print(f"{id} in college_keys!!!!!!!")

        except:
            print(f"{id} not in college_keys")



def add_new_colleges_to_key_list():
    new_data = []

    with open("../../fixtures/colleges_seeds.json") as file:
        data = json.load(file)

        for item in data:
            pk = item['pk']
            unit_id = item['fields']['unit_id']
            new_data.append({unit_id: {'pk': pk}})

    with open('college_keys.json', 'w') as outfile:
        json.dump(new_data, outfile, indent=4, sort_keys=True)


def find_all_pks():
    pks = []

    with open("../../fixtures/colleges_seeds.json") as file:
        data = json.load(file)

        for item in data:
            pk = item['pk']
            pks.append(pk)

    pks.sort()

    with open('all_pks.json', 'w') as outfile:
        json.dump(pks, outfile, indent=4, sort_keys=True)

def find_missing_pks():
    counter = 1
    missing_pks = []

    with open("all_pks.json") as file:
        data = json.load(file)

        for num in range(data[0], data[-1]+1):
                if num not in data:
                    missing_pks.append(num)

    with open('missing_pks.json', 'w') as outfile:
         json.dump(missing_pks, outfile, indent=4, sort_keys=True)
