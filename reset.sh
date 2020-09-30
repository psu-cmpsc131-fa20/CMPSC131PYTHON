#!/bin/sh
echo "Initializing reset of cmpsc131python repository..."

echo "Creating backup..."
git add .
git commit -m "All your old stuff"
git checkout -b backup
git push origin backup
echo "...done"

echo "Rolling back commits..."
git checkout b00ad82272133adbe0bc8b4f639c90829ccb01c0
git branch -D master
git checkout -b master
echo "...done"

echo "Running setup..."
git remote add staff https://github.com/psu-cmpsc131-fa20/CMPSC131PYTHON.git
git pull staff master --allow-unrelated-histories
git push -u origin -f master
echo "...done"
