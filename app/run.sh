#!/bin/bash

echo "DJANGO SETUP => STARTING..."

echo "DJANGO SETUP: CREATING VIRTUAL ENVIRONMENT"
cd backend
python3 -m venv .venv
source .venv/bin/activate

echo "DJANGO SETUP: INSTALLING DEPENDENCIES"
pip install -r requirements.txt

echo "DJANGO SETUP: RUN SERVER IN BACKGROUND"
cd server
python3 manage.py runserver 3000 &

echo "DJANGO SETUP => DONE"


echo ""
echo "RETURN TO INITIAL STATE => STARTING..."
echo "RETURN TO INITIAL STATE: RETURN TO APP FOLDER"
cd ../..
echo "RETURN TO INITIAL STATE => DONE"
