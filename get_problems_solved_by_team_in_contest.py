import urllib2
import json
from bs4 import BeautifulSoup

def parse_team_names(input) :
	return input.strip().replace('\n',',').split(',')

def parse_contests(input) :
	return input.strip().replace(' ',',').replace('\n',',').split(',')

teams_file = open("input.txt",'r')
contests_file = open("contests_input.txt",'r')
output_file = open("output.txt",'w')

team_names = list(set(parse_team_names(teams_file.read())))
contests_ids = list(set(parse_contests(contests_file.read())))

url = "http://codeforces.com/api/contest.status?"

solved_problems_by_team = dict()
for i in team_names :
	solved_problems_by_team[i] = set()

for i in range(0,len(contests_ids)) :
	cur_team_submissions = json.loads(urllib2.urlopen(url+"contestId="+contests_ids[i]+"&from=1&count=50000").read())
	output_file.write("Contest id "+ contests_ids[i] + ":\n")
	for j in cur_team_submissions["result"] :
		if "teamName" in j["author"]  and j["author"]["teamName"] in team_names:
			if j["verdict"] == "OK" :
				solved_problems_by_team[j["author"]["teamName"]].add(j["problem"]["name"])
	
	for team_name, problems in solved_problems_by_team.iteritems() :
		output_file.write("--Team " + team_name.encode("utf8") + " solved:\n")
		for k in problems :
			output_file.write("----" + k.encode("utf8") + '\n')
output_file.close()
print("DONE!")