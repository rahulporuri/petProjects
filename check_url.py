'''
https://gist.github.com/fedir/5883651
https://gist.github.com/dehowell/884204
http://stackoverflow.com/questions/16778435/python-check-if-website-exists
https://pythonadventures.wordpress.com/tag/url/
http://stackoverflow.com/questions/6471275/python-script-to-see-if-a-web-page-exists-without-downloading-the-whole-page

'''
import httplib

url_list = ['www.iitm.ac.in', 'www.physics.iitm.ac.in', 'www.physics.iitm.ac.in/~sriram', 'www.physics.iitm.ac.in/sriram']
'''
for url in url_list:
	c = httplib.HTTPConnection(url)
	c.request("HEAD",'')
	if c.getresponse().status == 200:
		print('website exists')

'''
import urllib2
for url in url_list:
	try :
		urllib2.urlopen('http://'+url)
	except urllib2.HTTPError, e:
		print (e.code)
	except urllib2.URLError, e:
		print (e.args)
