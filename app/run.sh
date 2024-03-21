#!/bin/bash

echo "DJANGO SETUP => STARTING..."

echo "DJANGO SETUP: CREATING VIRTUAL ENVIRONMENT"
cd backend
python3 -m venv .venv
source .venv/bin/activate

echo "DJANGO SETUP: INSTALLING DEPENDENCIES"
pip install -r requirements.txt &>/dev/null

echo "DJANGO SETUP: MIGRATING DATABASE"
cd server
python3 manage.py migrate &>/dev/null

echo "DJANGO SETUP: STARTING SERVER ON BACKGROUND"
python3 manage.py runserver 3000 &>/dev/null &
echo "DJANGO SETUP => PID: $!"

echo "DJANGO SETUP => DONE"


echo ""
echo "RETURN TO INITIAL STATE => STARTING..."
echo "RETURN TO INITIAL STATE: RETURNING TO APP FOLDER"
cd ../..
echo "RETURN TO INITIAL STATE => DONE"
echo ""


echo "VUE SETUP => STARTING..."

echo "VUE SETUP: INSTALLING DEPENDENCIES"
cd frontend
npm i &>/dev/null

echo "VUE SETUP: BUILDING PROJECT"
npm run build &>/dev/null

echo "VUE SETUP: STARTING SERVER ON BACKGROUND"
npm run preview &>/dev/null &
echo "VUE SETUP => PID: $!"

echo "VUE SETUP => DONE"

echo ""
echo "RETURN TO INITIAL STATE => STARTING..."
echo "RETURN TO INITIAL STATE: RETURNING TO APP FOLDER"
cd ..
echo "RETURN TO INITIAL STATE => DONE"
echo ""

echo "=== SUCCESS - SETUP CONCLUDED ==="
echo ""
echo "FRONTEND >> http://localhost:8080"
echo "BACKEND >> http://localhost:3000/travels"
echo ""
echo "SUBMISSION BY ADRIEL SANTOS"
echo "https://github.com/br-adriel"
echo ""
echo "================================="
