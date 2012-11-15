#!/usr/bin/python

import requests
import json

answerformat='json'
billId='S1234-2011'
host='http://open.nysenate.gov/legislation/2.0/bill/'

requesturl=host+billId+'.'+answerformat

print requesturl

response = requests.get(requesturl)

print response.json
