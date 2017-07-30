import urllib2
import json
from bs4 import BeautifulSoup

def parse_handles(input) :
	return input.strip().replace(' ',',').replace('\n',',').split(',')

def parse_problems(input) :
	return input.strip().replace('\n',',').split(',')

handles_file = open("input.txt","r")
problems_file = open("problems_input.txt","r")
output_file = open("output.txt","w")

handles = list(set(parse_handles(handles_file.read())))
problem_names = list(set(parse_problems(problems_file.read())))

link = "http://codeforces.com/api/user.status?"

for i in range(0,len(handles)) :
	cur_handle_submissions = json.loads(urllib2.urlopen(link+"handle="+handles[i]+"&from=1&count=10000").read())
	output_file.write(handles[i]+" solved:\n")
	accepted_problems = set()
	for j in cur_handle_submissions['result'] :
		if j["problem"]["name"] in problem_names and j["verdict"]=="OK":
			accepted_problems.add(j["problem"]["name"])
	for j in accepted_problems :
		output_file.write(j+'\n')

print("DONE!")