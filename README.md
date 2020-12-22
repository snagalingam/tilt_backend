# Run Backend with Docker

## Start App
1. Download and run Docker Desktop: https://www.docker.com/products/docker-desktop
2. To start the backend, run `docker-compose up -d --build`
3. To get the database up and running, run `docker-compose exec backend python3 manage.py migrate`

## Shut Down
1. To shut down the instances of Docker, run `docker-compose down`

# Run Backend with Virtual Environment

## Set up backend environment
1. Install virtualenv to work with virtual environments:
      - RUN `pip install virtualenv`
2. Create virtual envrionment in any directory
      - RUN `virtualenv <name of virtual environment>`
3. Activate virtual envrionment:
      - RUN `source <name of virtual environment>/bin/activate`
4. Install dependencies
      - RUN `pipenv install`

## Set up local database
Create local db instance using postgres. Easiest way: https://postgresapp.com/

## Set environment variables
1. `export ENVIRONMENT="development"`
2. `export DEBUG=1`
3. `export SECRET_KEY={'<any_random_string>'}`
4. `export REGION="us-east-2"`
5. `export DATABASE_HOST="{local db host}"``
6. `export DATABASE_NAME="{local db name}"`
7. `export DATABASE_PASSWORD="{local db password}"`
8. `export DATABASE_USER="{local db user}"`

## Update local database
Execute `python3 manage.py migrate` to run the migrations on your local database instance.

## Start server
RUN `python3 manage.py runserver`
