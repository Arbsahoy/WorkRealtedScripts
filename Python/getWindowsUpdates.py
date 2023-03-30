#Import required modules to test if they are installed
import importlib.util as iutil
import os

rqts = ['selenium']

print('Checking for required modules...')

for r in rqts:
    if iutil.find_spec(r) is None:
        print('Installing ' + r + '.')
        os.system('! pip install ' + r)
    else:
        print(r + ' is installed.')

# Import required modules to finish the script
import time as t
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

#open browser of choice, being MSFT let's use Edge! 
driver = webdriver.Edge()

#Makes the window that opened in the last line to full screen
driver.maximize_window()

#send the browser to the URL of interest
driver.get('https://www.catalog.update.microsoft.com/Search.aspx?q=windows%2010%20cumulative%20update')

#look for the element that contains the table id information
tableOfInterest = driver.find_element(By.ID,'ctl00_catalogBody_updateMatches')

rows = tableOfInterest.find_elements(By.TAG_NAME, 'tr')

for row_data in rows:
    col = row_data.find_elements(By.TAG_NAME, "td")
    for i in range(len(col)):
        print(col[i].text)

#generate a log file that saves the printed above.
#look at old log file to see the last one used


#it's best practice to close the browser when you're done
driver.close()