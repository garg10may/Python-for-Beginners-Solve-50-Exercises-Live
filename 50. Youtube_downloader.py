
from urllib2 import urlopen
from urlparse import unquote
import re

url ='https://www.youtube.com/watch?v=Wt1wFf53e2o'
response = urlopen(url)
content = response.read()
direct_urls = re.findall(r'"url_encoded_fmt_stream_map":.*?url=(https.*?)(,|\\u0026)', content)

direct_url = unquote(direct_urls[0][0])

d = urlopen(direct_url)
f = open('Test_video.avi', 'wb')

f.write(d.read())

d.close()l
f.close()






