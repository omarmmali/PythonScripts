import urllib2
import json
from bs4 import BeautifulSoup

def parse(input) :
	return input.strip().replace(' ',',').replace('\n',',').split(',')

handles_file = open("input.txt",'r')
contests_file = open("contests_input.txt",'r')
output_file = open("output.txt",'w')

handles = list(set(parse(handles_file.read())))
contests_ids = list(set(parse(contests_file.read())))

url = "http://codeforces.com/api/contest.status?"

solved_problems_by_handle = dict()
for i in handles :
	solved_problems_by_handle[i] = set()

for i in range(0,len(contests_ids)) :
	cur_team_submissions = json.loads(urllib2.urlopen(url+"contestId="+contests_ids[i]+"&from=1&count=50000").read())
	output_file.write("Contest id "+ contests_ids[i] + ":\n")
	for j in cur_team_submissions["result"] :
		if j["verdict"] == "OK" :
			for k in j["author"]["members"] :
				if k["handle"] in handles :
					solved_problems_by_handle[k["handle"]].add(j["problem"]["name"])

	
	for handle, problems in solved_problems_by_handle.iteritems() :
		if len(problems) < 1 :
			continue
		output_file.write("--Handle " + handle.encode("utf8") + " solved:\n")
		for k in problems :
			output_file.write("----" + k.encode("utf8") + '\n')
output_file.close()
print("DONE!")