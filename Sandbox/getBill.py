#!/usr/bin/python

import requests
import json

billId='S1234-2011'
host='http://open.nysenate.gov/legislation/bill/'

url=host+billId

response = requests.get(url)

print response.text
