# django-simple-login-register
Simple django register and login authentication for demo

## Setting up PostGreSql
> sudo apt update

> sudo apt-get -y install postgresql-14

> sudo service postgresql start

> sudo -u postgres psql

> CREATE DATABASE login_reg_auth_db;

> \c login_reg_auth_db

> CREATE USER fritz WITH PASSWORD 'adminfritz';

> GRANT TEMP ON DATABASE login_reg_auth_db TO fritz;

> GRANT ALL PRIVILEGES ON DATABASE login_reg_auth_db TO fritz;

> GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO fritz;

## Setup
> pipenv install

> pipenv shell # install dependencies

> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
