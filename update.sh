#!/bin/sh
git add .
git commit -m "Any uncommitted changes."
git fetch --unshallow origin
git pull staff master --allow-unrelated-histories --no-edit
git push origin master
