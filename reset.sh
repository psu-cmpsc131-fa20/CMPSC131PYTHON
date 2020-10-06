#!/bin/sh
echo "Initializing reset of cmpsc131python repository..."

echo "Creating backup..."
git add .
git commit -m "All your old stuff"
branch=backup.$(date +"%s")
git checkout -b $branch
git push origin $branch
echo "...done"

echo "Rolling back commits..."
git branch -D master
git checkout -b master 4741ebdd0e1b7a55b2f28261a3ff62f45da9b18a 
echo "...done"

echo "Running setup..."
git remote add staff https://github.com/psu-cmpsc131-fa20/CMPSC131PYTHON.git
git pull staff master --allow-unrelated-histories --no-edit
git push -u origin -f master
echo "...done"
