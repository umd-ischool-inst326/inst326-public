import requests
import xml.etree.ElementTree  

podcast = requests.get("http://feed.thisamericanlife.org/talpodcast")
root  = xml.etree.ElementTree.fromstring(podcast.content)
print(root)
for item in root.iter("item"):
	for attribute in item.iter("title"):
		#print ("Tag: " + attribute.tag)
		print (attribute.text)		