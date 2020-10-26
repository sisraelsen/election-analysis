import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://electionstudies.org/anes_timeseries_cdf/'

print('Retrieving', url)
filedata = urllib.request.urlopen(url, context=ctx)
datatowrite = filedata.read()
with open('data.zip', 'wb') as f:
    f.write(datatowrite)

# Unzip the zip file
import os
os.system('unzip -d data data.zip')
