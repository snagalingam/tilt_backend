import os
import json
import requests
from urllib.parse import urlencode

def get_photo_url(file_name):
    colleges = json.load(open(f'{file_name}.json'))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit537.36(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    for college in colleges[0:]:
        pk = college.get('pk')
        fields = college.get('fields')
        place_id = fields.get('place_id')
        name = fields.get('name')
        photos = fields.get('photos')
        main_photo = fields.get('main_photo')

        if len(main_photo) > 0:
            try:
                response = requests.get(main_photo, headers=headers)
                main_photo_url = response.url
            except Exception as e:
                print(e)
                
        else:
            main_photo_url = main_photo

        photo_urls = []
        if len(photos) > 0:
            for p in photos: 
                res = requests.get(p, headers=headers)
                photo_urls.append(res.url)

        data = {
            'place_id': place_id,
            'name': name,
            'main_photo': main_photo_url,
            'photos': photo_urls,
        }

        # print(f'  ==> pk: {pk} / name: {name}')
        # with open(f'photo_urls.json', 'a+') as f:
        #     scorecard_data = json.dumps(data, indent=2, ensure_ascii=False)
        #     f.write(scorecard_data + ',')

    return print(f'  ==> FINISHED: {file_name}')


def replace_photos(file_1, file_2):
    colleges = json.load(open(f'{file_1}.json'))
    photo_urls = json.load(open(f'{file_2}.json'))

    for p in photo_urls:
        p_place_id = p.get('place_id')
        p_main = p.get('main_photo')
        p_photos = p.get('photos')

        for c in colleges: 
            pk = c.get('pk')
            f = c.get('fields')
            c_place_id = f.get('place_id')
            c_main = f.get('main_photo')
            c_photos = f.get('photos')

            if p_place_id == c_place_id:
                print(f"  {pk} ===> name: {c['fields']['name']}")
                c['fields']['main_photo'] = p_main
                c['fields']['photos'] = p_photos

                # with open(f'new_colleges.json', 'a+') as f:
                #     data = json.dumps(c, indent=2, ensure_ascii=False)
                #     f.write(data + ',')
                # break
        
    return print(f'  ==> FINISHED: {file_1} + {file_2}')
