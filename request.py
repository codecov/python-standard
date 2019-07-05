#testing to see if I can hit the CC API and return coverage stats
import requests
import urllib
import time

payload = {'token': '11412e01-7ed6-4d72-b438-d8a297eced21'}
link = 'https://codecov.io/api/gh/ibrahim0814/pystandard-draft'

time.sleep(60)

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