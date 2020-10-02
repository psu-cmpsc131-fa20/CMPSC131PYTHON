git commit -a -m "commit before update by staff"
git pull staff master --allow-unrelated-histories --no-edit
git commit -a -m "commit after merge by staff"
git push origin master
