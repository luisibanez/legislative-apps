#!/usr/bin/python

#
# http://openlegislation.readthedocs.org/en/latest/#meeting
#

import requests
import json
import sys

if len(sys.argv) < 2:
  sys.exit('Missing Argument. The arguments should be <regular|special> Date: such as: regular 08-03-2011')

transcriptID=sys.argv[1]+'-session-'+sys.argv[2]

answerformat='json'
host='http://open.nysenate.gov/legislation/2.0/transcript/'

requesturl=host+transcriptID+'.'+answerformat

print requesturl

response = requests.get(requesturl)

print json.dumps(response.json)

