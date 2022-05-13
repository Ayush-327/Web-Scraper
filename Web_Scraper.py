# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:25:24 2022

@author: hp
"""

from bs4 import BeautifulSoup
import requests
import time



unfamilier_skills = [item for item in input("Enter the unfamilier skills : ").split()]
print("Filtering out")
print(unfamilier_skills)

def find_jobs():    
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):   
     published_date = job.find('span', class_= 'sim-posted').text
     if 'few' in published_date:
         skills = job.find('span' , class_='srp-skills').text
         results =[]
         for skill in unfamilier_skills:
             results.append(skill in skills)
         
         if True not in results:
             company_name = job.find('h3', class_='joblist-comp-name').text
             with open(f'Posts/{index}.txt', 'w') as f:
              f.write(f'Company name: {company_name.strip()}\nSkills: {skills.strip()}')
              print(f'File {index}.txt saved')
              print(skills)
#             print('--------------------------------------------------------------')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting:{time_wait}minutes')
        time.sleep(time_wait*60)

