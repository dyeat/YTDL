import requests #2015-09-29 youtube影片爬蟲
res = requests.get('影片網址')
# print res.text

import re
m = re.search('"args":({.*?}),', res.text) #擷取args內容
# print m.group(1)
import json
jd = json.loads(m.group(1))
# print jd["url_encoded_fmt_stream_map"]

import urlparse
a = urlparse.parse_qs(jd["url_encoded_fmt_stream_map"])
# print a

print a['url'][0]
import shutil
res2 = requests.get(a['url'][0], stream=True)
f = open('a.mp4','wb') #另外生成一個檔名為a.mp4
shutil.copyfileobj(res2.raw, f)
f.close()