#!/usr/bin/python

import requests
import json
import sys

if len(sys.argv) < 2:
  sys.exit('Missing Argument. The argument should be a Bill Id such as: S1234-2011')

billId=sys.argv[1]

answerformat='json'
host='http://open.nysenate.gov/legislation/2.0/bill/'

requesturl=host+billId+'.'+answerformat

response = requests.get(requesturl)

print response.json

