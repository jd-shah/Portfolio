# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:04:17 2020

@author: shahj

Github Classroom is used to share assignments with students.
If class is programming based, one might need to share "issues" with each student as a part of the 
assignment. 
This feature isn't available in Github Classroom yet.
Till they release the official feature, this is the script that can be used to do that manually for
all students.
"""

"""
Library used: PyGithub - https://pygithub.readthedocs.io/en/latest/index.html 
"""

"""
Algorithm:
    
"""

import json
from github import Github

#Assignment Prefix; to identify assignment repos of students
#Issue title; one that needs to be added
#Issue body; one that needs to be added
stud_repo_prefix = "week-6"
issue_title = "Issue 3 from python"
issue_body = "There would be a formatted content"

#Fetch Github Credentials frmo JSON file
with open('./creds.json') as cred:
    credential = json.load(cred)
cred.close

#Log in to the account:
git_account = Github(credential["git-account"],credential["git-password"])

for repo in git_account.get_user().get_repos():
    r_name = repo.name
    if(r_name.startswith(stud_repo_prefix)):
        print(r_name)
        
        #check if there exist the expected issue
        issue_exist = False
        s_issues = repo.get_issues(state="open")
        for s_issue in s_issues:
            if(s_issue.title == issue_title):
                issue_exist = True
                break
        
        #if not then add the issue to the repo
        if(issue_exist == False):
            repo.create_issue(title = issue_title, body = issue_body)
        else:
            print("Issue exist in this repo")
            