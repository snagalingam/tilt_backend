# ========== !!! IMPORTANT!!! ==========

1. Dump data FIRST
2. THEN edit fixure files
3. THEN load (RESEED) files
4. `otherwise you will lose your current data`


# Examples of Tilt db table names

1. colleges.College
2. colleges.Scorecard
3. colleges.FieldOfStudy
4. colleges.Status
5. organizations.Organization
6. financial_aid.Category
7. financial_aid.Data


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

3. Make edits on dumped file 

4. Load (seed) edited file
    `python manage.py loaddata fixtures/colleges.json`


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
