'''Make a Python script which downloads the You tube video. The video should be saved for future use.'''


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

#This will save the video to your default path. To change path use os.chdir(path)
#Also note this will read the whole file into the memory and than write. We did this to make it words shortest script.
#Instead read a chunk and write till complete. 
f.write(d.read())

d.close()
f.close()






