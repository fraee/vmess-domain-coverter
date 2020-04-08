import socket
from urllib.request import urlopen, Request
from base64 import b64decode, b64encode
import json
from retrying import retry


@retry(stop_max_attempt_number=3)
def get_links(req):
    print('Trying to get links...')
    return urlopen(req, timeout=20).read()


subscribe_url = '< Your subscription link >'
ua = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.88 Safari/537.36'}
info_req = Request(subscribe_url, headers=ua)
return_content = get_links(info_req)

if not return_content:
    print('Got nothing, exit.')
    exit()
else:
    missing_padding = 4 - len(return_content) % 4
    if missing_padding:
        return_content += b'=' * missing_padding
vmess_links = b64decode(return_content).decode('utf-8').splitlines()

convert = ''
for vl in vmess_links:
    jn = json.loads(b64decode(vl.replace('vmess://', '')).decode('utf-8'))
    print('domain:' + jn['add'])
    try:
        ip = socket.getaddrinfo(jn['add'], None)[0][4][0]
    except Exception as reason:
        print(reason)
        print('Get ip failed, continue...')
    else:
        jn['add'] = ip
        print(jn)
    base64link = b64encode(json.dumps(jn).encode())
    base64decode = 'vmess://' + base64link.decode('utf-8')
    convert += base64decode + '\n'

filename = '< /your/file/path >'
with open(filename, 'w') as file_obj:
    file_obj.write(str(b64encode(convert.encode()), 'utf-8'))
