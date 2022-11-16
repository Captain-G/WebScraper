from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skill = input("Put some skill that you are not familiar with : ")

print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    # lxml is a library for parsing xml and html

    counter = 1
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        # enumerate allows us to iterate over the index of the jobs list and the job content itelf
        # index is the counter

        published_date = job.find('span', class_='sim-posted').text.replace(" ", "")

        if "few" in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ", "")
            skills = job.find('span', class_='srp-skills').text.replace(" ", "")
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'Posts/{index}.txt', 'w') as f:
                    f.write(f"{counter}.Company name : {company_name.strip()}\n")
                    f.write(f"Required skills : {skills.strip()}\n")
                    f.write(f"More info : {more_info}\n")
                print(f"File saved : {index}")
                counter += 1


if __name__ == '__main__':
    # it allows you to execute code when the file runs as a script but not when it is imported as a module
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
