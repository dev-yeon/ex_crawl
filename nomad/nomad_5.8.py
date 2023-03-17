
# 5.8 Saving Results  :성가신html 태그를 제거하기 위해 .string 라는 bs elements를 사용해보자.

from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website.")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')  # list 안의 모든 anchor 을 찾되,
            anchor = anchors[1] # 회사의 로고는 필요 없다.
            # beautiful soup의 좋은점 1:  html 태그 들이 dictionary 처럼 바뀐다.  파이선 dictionary 처럼 쓸 수 있다 .
            link = anchor['href']  # anchor 안의 span 에 접근 하고 싶다.  회사 이름. 직업 이름, 상근직 원격직, 위치
            company, kind, region = anchor.find_all('span', class_="company")

            title = anchor.find('span', class_='title')
            # 성가신html 태그를 제거하기 위해 .string 라는 bs elements를 사용해보자.

    # 출력 결과 : Trustworthy Full-Time Anywhere in the World Full Stack Software Engineer (React / Python)
        job_data = {
            'company': company.string,
            'region': region.string,
            'position': title.string
        }
        results.append(job_data)
        # 이 말의 뜻은, 우리가 job을 추출할 때마다. 그것들을 list안에 넣을 것이란 것을 뜻한다.

        #이 job_data의 dictionary는 재생성될것이다, 왜냐하면
        #  페이지의 각 section 에서 재생성되는 list 안의 각각의 post 때문에,
        # for_loop의 바깥쪽에 저장해야한다.



    print(results)


