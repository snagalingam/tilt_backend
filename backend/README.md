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

## Setup local database instance:
1. Create local db instance using postgres. Easiest way: https://postgresapp.com/
2. Update `DATABASE` variable in `backend/tilt/project/settings.py` with the name, user, pass, etc. of your local instance.
      - Remember to not commit these changes
3. Execute `python3 manage.py migrate` to run the migrations on your local database instance.

## Add to .env file:
1. `export SENDGRID_API_KEY="api_key"`
2. `export SECRET_KEY="generate_random_string"`
3. `export DOMAIN="http://127.0.0.1:8000"`

4. `export GOOGLE_API="api_key"`

5. `export DB_NAME="local_db_name"`
6. `export DB_USER="local_db_user"`
7. `export DB_PASSWORD="local_db_password"`

## Start Server

RUN `python3 manage.py runserver`
