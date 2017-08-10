import urllib2
import json
from bs4 import BeautifulSoup

url = "http://codeforces.com/api/contest.status?contestId=101020&from=1&count=5"


response = urllib2.urlopen(url).read()
response = json.loads(response)

print(response['result'][4]['author']['teamName'])