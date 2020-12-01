# Author: Yanling Wang yuw17@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 1

from matplotlib import pyplot as plt

# Retrieve a list of counties from argv[2]
counties = ['Centre']

# Retrieve the number of days from argv[3]
days = 10 

plt.xticks(rotation=70, fontsize=6)
plt.ylabel('7-day Average New Cases per 100,000 population')

# Write code to read csv file (argv[1]) into a list of dictionaries

for county in counties: 
  # Retrieve from the csv file's data x/y data for a specific county 
  # The length of the data should match the number of days from argv[3]
  # It should be data for the most recent days. 
  county_ys = list(range(days)) 
  county_dates = list(range(days)) 
  plt.plot(county_ys, label = county)
  if days > 30:
    plt.xticks(range(0,days,7), county_dates[::7])
  else:
    plt.xticks(range(days), county_dates)


plt.legend()
# Save figure to the file argv[4]
plt.savefig('sample.png')
plt.show()
