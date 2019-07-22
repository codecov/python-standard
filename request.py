#testing to see if I can hit the CC API and return coverage stats
import requests
import urllib
import time
import os

payload = {'token': os.environ['API_KEY']}
link = 'https://codecov.io/api/gh/codecov/Python-Standard'

time.sleep(180)

#get latest coverage data
all_data = requests.get(link, params=payload).json()

commit_data = all_data['commits'][0]

coverage_percentage = commit_data['totals']['c']

#result should return 85.71429 as its coverage metric
if(coverage_percentage == '85.71429'): 
    print("success!")
    exit(0)
else:
    print("something is wrong")
    exit(1)