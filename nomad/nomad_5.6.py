

"""

"""
# 5.6 Job Posts : 새로운 내장 기능에 대해 알아보기

# 5.4 Beautiful Soup
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.find_all('title')) # [<title>We Work Remotely: Advanced Remote Job Search</title>]
    jobs = soup.find_all('section', class_="jobs")  # print(len(jobs)) #jobs 클래스를 가진 section은 총 몆개 받았나요?  ==>3
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1) # 제일 마지막의 li= view-all을 지우고 싶다.
        for post in job_posts:
            print(post)
            print("///////////////////")

# beautiful soup는 HTML 문서를 python문법으로 바꾸어준다.
