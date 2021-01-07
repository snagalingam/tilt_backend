# ========== !!! IMPORTANT!!! ==========

1. Dump data FIRST
2. THEN edit fixure files
3. THEN load (RESEED) files
4. `otherwise you will lose your current data`


# Examples of Tilt db table names

1. aid.AidCategory
2. aid.AidData
3. college.College
4. college.Scorecard
5. college.FieldOfStudy
6. college.CollegeStatus
7. organization.Organization

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
    `./manage.py dumpdata college.college --indent 2 --format json > fixtures/colleges.json`

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
