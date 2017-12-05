import pycurl
import json
from io import BytesIO



buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://ip-ranges.amazonaws.com/ip-ranges.json')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
json1_data = json.loads(body.decode('iso-8859-1'))
print('# cloudront dynamic IP range, taken from https://ip-ranges.amazonaws.com/ip-ranges.json')
for majorkey in json1_data['prefixes']:
    if 'CLOUDFRONT' in majorkey['service']:
        print("set_real_ip_from\t" + majorkey['ip_prefix'] + ";")


