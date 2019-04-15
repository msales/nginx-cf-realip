import pycurl
import json
from io import BytesIO


cloudflare_real_ip = [
    '173.245.48.0/20',
    '103.21.244.0/22',
    '103.22.200.0/22',
    '103.31.4.0/22',
    '141.101.64.0/18',
    '108.162.192.0/18',
    '190.93.240.0/20',
    '188.114.96.0/20',
    '197.234.240.0/22',
    '198.41.128.0/17',
    '162.158.0.0/15',
    '104.16.0.0/12',
    '172.64.0.0/13',
    '131.0.72.0/22',
    '2400:cb00::/32',
    '2405:b500::/32',
    '2606:4700::/32',
    '2803:f800::/32',
    '2c0f:f248::/32',
    '2a06:98c0::/29',
    '2400:cb00::/32',
    '2606:4700::/32',
    '2803:f800::/32',
    '2405:b500::/32',
    '2405:8100::/32',
    '2a06:98c0::/29',
    '2c0f:f248::/32'
]



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

for real_ip in cloudflare_real_ip:
    print("set_real_ip_from\t" + real_ip + ";")
