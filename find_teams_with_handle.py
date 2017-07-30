import urllib2
import re
from bs4 import BeautifulSoup

input_file = open("input.txt","r")
output_file = open("output.txt","a")

handles = list(set(input_file.read().strip().replace(' ',',').replace('\n',',').split(',')))

team_link = "http://codeforces.com/teams/with/"

for i in range(0,len(handles)) :
	cur_page = urllib2.urlopen(team_link+handles[i]).read()
	cur_soup = BeautifulSoup(cur_page,"lxml").find("div",class_="teamlist").find("div",class_="datatable").find_all('a')
	output_file.write(handles[i]+':\n')
	for i in cur_soup :
		if "team" in i["href"]:
			output_file.write(i.string+'\n')
output_file.close()
print("DONE!")
