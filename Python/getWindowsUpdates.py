import importlib.util as iutil
import os

rqts = ['requests', 'selenium']

print('Checking for required modules...')

for r in rqts:
    if iutil.find_spec(r) is None:
        print('Installing ' + r + '.')
        os.system('! pip install ' + r)
    else:
        print(r + ' is installed.')

import requests
import json
import time as t
from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Edge()

driver.maximize_window()
driver.get('https://www.catalog.update.microsoft.com/Search.aspx?q=windows%2010%20cumulative%20update')












driver.close()