# Tilt Backend

## Set up backend locally
1. Install virtualenv to work with virtual environments:
      - RUN `pip install virtualenv`
2. Create virtual envrionment in any directory (easier to manage if in backend director)
      - RUN `virtualenv <name of virtual environment>`
3. Activate virtual envrionment: 
      - RUN `source <name of virtual environment>/bin/activate`
4. Install dependencies
      - RUN `pipenv install`
      - RUN `pip install -r requirements.txt`

## Setup local database instance:
1. Create local db instance using postgres. Easiest way: https://postgresapp.com/
2. Update `DATABASE` variable in `backend/tilt/project/settings.py` with the name, user, pass, etc. of your local instance.
      - Remember to not commit these changes
3. Execute `python3 manage.py migrate` to run the migrations on your local database instance.

## To run local development mode, run following commands in terminal:
1. `export ENVIRONMENT="development"`
2. `export DEBUG=1`
3. `export SECRET_KEY={'<any_random_string>'}`

## Start Server

RUN `python3 manage.py runserver`
