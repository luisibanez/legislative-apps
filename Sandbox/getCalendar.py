#!/usr/bin/python

#
# http://openlegislation.readthedocs.org/en/latest/#meeting
#

import requests
import json
import sys

if len(sys.argv) < 2:
  sys.exit('Missing Argument. The arguments should be Floor Date: such as: floor 06-24-2011')

meetingId=sys.argv[1]+'-'+sys.argv[2]

answerformat='json'
host='http://open.nysenate.gov/legislation/2.0/calendar/'

requesturl=host+meetingId+'.'+answerformat

response = requests.get(requesturl)

print json.dumps(response.json)

