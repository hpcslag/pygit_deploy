# coding=utf-8
from github import Github #PyGithub module (pip, python -m pip install PyGithub)
import sys
import datetime
from dateutil.parser import parse
import pytz
import time
import urllib
import os
from subprocess import call

utc = pytz.UTC

def rtn_repo(name,g):
	for repo in g.get_user().get_repos():
		if repo.name == name:
			return repo
	return None

def show_commit_date(commits):
	for commit in commits:
		print commit.commit.last_modified

def get_last_commit_date(commits):
	return parse(commits[0].commit.last_modified).replace(tzinfo=utc)

def get_committer(commits):
	return commits[0].committer.name

def get_commit_message(commits):
	return commits[0].commit.message

def init_new_commits():
	usr = sys.argv[1]
	pwd = sys.argv[2]
	g = Github(usr,pwd)

	current_repo = rtn_repo(sys.argv[3],g)

	if current_repo == None:
		print "can't found this repo in your github"
		exit()

	return current_repo.get_commits()


try:
	commits = init_new_commits()

	last_check_last_update = get_last_commit_date(commits = commits)
	now_check_last_update = get_last_commit_date(commits = commits)

	os.chdir(sys.argv[4])
	
	while(True):
		commits = init_new_commits()
		now_check_last_update = get_last_commit_date(commits = commits)

		if(last_check_last_update < now_check_last_update):
			last_check_last_update = now_check_last_update
			print u'Found New Commit Version - @'+get_committer(commits)+' :  '+get_commit_message(commits)
			call(["git","pull"])

		time.sleep(5)


except IndexError:
	print "Your argumnets need give username and password to login your github repo"


