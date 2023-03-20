
# 5.9 Recap
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term=" # 바뀌지 않는 url
search_term = "java"
# 내가 검색어 를 뭘로 치느냐 에 따라 바뀌는 단어

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website.")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    # response.text 는 방금 검색한 웹 사이트 의 코드를 주고, 우리는 그걸 beautiful soup 에게 준다.
    # 웹 사이트 의 내용 으로 bs를 호출 하면, 우리는 그 코드 안에서 검색을 해 볼 수 있다 .
    jobs = soup.find_all('section', class_="jobs")  #class의 이름이 jobs인 섹션을 찾아보기.
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1) # 제일 마지막 줄의 view all 은 그냥 버튼 이라 읽고 싶지 않아서 마지막 항목을 지웠다.

        for post in job_posts:
            anchors = post.find_all('a')  # list 안의 모든 anchor 을 찾되,
            anchor = anchors[1] # 회사의 로고는 필요 없다.
            # beautiful soup의 좋은점 1:  html 태그 들이 dictionary 처럼 바뀐다.  파이선 dictionary 처럼 쓸 수 있다 .
            link = anchor['href']  # anchor 안의 span 에 접근 하고 싶다.  회사 이름. 직업 이름, 상근직 원격직, 위치
            company, kind, region = anchor.find_all('span', class_="company") # 우리가 만든 변수에 찾은 내용을 넣고 싶다고 파이선 에게 알려 주기

            title = anchor.find('span', class_='title')
            # find 는 하나의 항목만 준다. /  find all 은 전부 준다
            # 성가신 html 태그를 제거 하기 위해 .string 라는 bs elements 를 사용해 보자.

    # 출력 결과 : Trustworthy Full-Time Anywhere in the World Full Stack Software Engineer (React / Python)

        job_data = {
            'link': f"https://weworkremotely.com{link}",
            'company': company.string,
            'region': region.string,
            'position': title.string
        } # 이 짓은 section 의 모든 list 에서 실행 되므로, for 문 밖에 저장 하지 않으면 사라 진다.
        results.append(job_data)
        # 이 말의 뜻은, 우리가 job 을 추출할 때마다. 그것 들을 list 안에 넣을 것이란 것을 뜻한다.

        #이 job_data의 dictionary는 재생성될것이다, 왜냐하면
        #  페이지의 각 section 에서 재생성되는 list 안의 각각의 post 때문에,
        # for_loop 의 바깥 쪽에 저장 해야 한다.



    print(results)


