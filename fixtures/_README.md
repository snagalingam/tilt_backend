# Examples of Tilt db table names 

1. colleges.college
2. colleges.scorecard
3. colleges.fieldofstudy
4. college_status.collegestatus
5. organizations.organization


# How to load (seed) data to database
`https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata`

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


# How to dump (extract) data from database

1. Dump entire database to file
    `./manage.py dumpdata --indent 2 --format json > fixtures/<file name>.json`

2.  Dump app data to file
    `./manage.py dumpdata <app name> --indent 2 --format json > fixtures/<file name>.json`

3.  Dump one table to file
    `./manage.py dumpdata <app name>.<table name> --indent 2 --format json > fixtures/<file name>.json`


# How edit data in the database with dumpdata and loaddata

1. Connect to staging database

2. Dump (extract) current data
    `./manage.py dumpdata colleges.college --indent 2 --format json > fixtures/colleges.json`

3. colleges.college (extract current data)
    `./manage.py dumpdata colleges.college --indent 2 --format json > fixtures/colleges.json`

4. colleges.college (extract current data)
    `./manage.py dumpdata colleges.college --indent 2 --format json > fixtures/colleges.json`