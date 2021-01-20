import requests
import feedparser

#how to read a file from the web
#page = requests.get("https://w1.weather.gov/xml/current_obs/KCGS.xml")
#print (page.text)

#how to read with feedparser
podcast = feedparser.parse("http://feed.thisamericanlife.org/talpodcast")
for i in range(len(podcast.entries)):
	print (podcast.entries[i].title)