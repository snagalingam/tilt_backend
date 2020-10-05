# How to seed in django 

1. Run
    `python manage.py loaddata fixtures/<file name>.json`

2. Fields
    `Unit ID, PE ID, Name, City, Zipcode`

3. Run all fixtures
   `python manage.py loaddata fixtures/*.json`

3. Delete all data in table
   `<model>.objects.all().delete()`