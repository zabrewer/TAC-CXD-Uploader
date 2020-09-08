# simple script to upload a file to a TAC SR using a Customer eXperience Drive (CXD) token
# Someone must generate the token from the case before running this script
# requires requests python module
# see https://www.cisco.com/c/en/us/support/web/tac/tac-customer-file-uploads.html#cxduploadtoken

import requests
from requests.auth import HTTPBasicAuth
import logging

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('TACFileUploader')

url = 'https://cxd.cisco.com/home/'

casenum = input('TAC case number:  ')
cxd = input('Customer eXperience Drive (CXD) token:  ')
filename = input('Filename to upload. Full path if not in same directory as this script:  ')

auth = HTTPBasicAuth(casenum, cxd)

try:
    f = open(filename, 'rb')
except Exception as e:
    print('\n\nFilename ' + "'" + filename + "'" + ' not found\n\n')
    print('Python error:\n' + str(e))
    exit(0)

try:
    r = requests.put(url + filename, f, auth=auth, verify=False)
    if r.status_code == 201:
        print('File successfully uploaded for TAC SR '+ casenum)
        r.close()
        f.close()
except Exception as e:
    logger.error('Failed to upload file for SR'+ casenum + '\n\n' + str(e))
    f.close()


