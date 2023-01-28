#!/bin/bash

# Stop on error
set -e
# Install requirements
pip install -r ./requirements.txt

# Setup database
psql -p $DB_PORT -d postgres -c "DROP DATABASE IF EXISTS  $DB_NAME WITH (FORCE);" #WITH FORCE = Postgres <=13
set +e
psql -p $DB_PORT -d postgres -c "DROP ROLE IF EXISTS $DB_USER;"
psql -p $DB_PORT -d postgres -c "CREATE ROLE $DB_USER with encrypted password '$DB_PASSWORD' login;"
set -e
psql -p $DB_PORT -d postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
psql -p $DB_PORT -d $DB_NAME -c "GRANT ALL ON SCHEMA public TO $DB_USER;"
psql -p $DB_PORT -d $DB_NAME -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# Prepare and run migrations
rm -f migrations/0*.py
python manage.py makemigrations account
python manage.py makemigrations parent
python manage.py makemigrations teachers
python manage.py migrate

# Prepare fixtures from Excel
python manage.py data_from_excel -f address/fixture/governorate.xlsx -a address 
python manage.py data_from_excel -f address/fixture/district.xlsx -a address
python manage.py data_from_excel -f address/fixture/subdistrict.xlsx -a address
python manage.py data_from_excel -f address/fixture/village.xlsx -a address
python manage.py data_from_excel -f address/fixture/subvillage.xlsx -a address
python manage.py data_from_excel -f address/fixture/location_type.xlsx -a address
python manage.py data_from_excel -f address/fixture/location.xlsx -a address
python manage.py data_from_excel -f address/fixture/school_gender.xlsx -a student
python manage.py data_from_excel -f address/fixture/school_shift.xlsx -a student
python manage.py data_from_excel -f address/fixture/School.xlsx -a student
