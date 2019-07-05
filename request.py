#testing to see if I can hit the CC API and return coverage stats
import requests
import urllib

payload = {'token': '11412e01-7ed6-4d72-b438-d8a297eced21'}
link = 'https://codecov.io/api/gh/ibrahim0814/pystandard-draft'

all_data = requests.get(link, params=payload).json()

commit_data = all_data['commits'][0]

coverage_percentage = commit_data['totals']['c']

if(int(coverage_percentage) == 100): 
    exit(1)
else:
     exit(0)