# How to seed in django 

1. Load one file
    `python manage.py loaddata fixtures/<file name>.json`

2. Load all files 
   `python manage.py loaddata fixtures/*.json`

3. Run Python Shell 
   `python manage.py shell`
   Import Models
   `from <app name>.models import <model>`
   Delete all data in table
   `<model>.objects.all().delete()`