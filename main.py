
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()

browser = webdriver.Chrome(options=options)
options.add_experimental_option("detach",True)
driver = webdriver.Chrome("./chromedriver.exe", options=options)
base_url = "https://kr.indeed.com/jobs?q="
pageload = driver.get('https://kr.indeed.com/jobs?q=python')
search_term = "python"

browser.get(f"{base_url}{search_term}")
results = []
#options.add_argument("--no-sandbox") # replit.it를 위한 코드 1
#options.add_argument("--disable-dev-shm-usage")# replit.it를 위한 코드 2



"""
base_url = "https://kr.indeed.com/jobs?q="
search_term = "임상병리사"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request page")
else:
    soup = BeautifulSoup(response.text, "html.parser")
"""
# indeed 가 request들을 막고 있어서, request 부분의 코드를 모두 삭제 하였다.
# browser을 사용해서 페이지의 HTML을 얻기 위해서.
# 셀레니움은 브라우저의 자동화를 가능하게 해준다.
# indeed가 봇이 정보를 긁는걸 막으니까.  위의 코드의 response를 건너 뛰고

soup = BeautifulSoup(browser.page_source,'html.parser')
job_list = soup.find('ul', class_='jobsearch-ResultsList')
jobs = job_list.find_all('li', recursive=False)

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:    #job li에서 job을 추출한다.
        anchor = job.select_one("a") # indeed 페이지 소스가 바뀌어서, <h2>태그와, <a href>태그를 나눠놨기 때문에,
        #select_one("h2 a") 로 하면 안되고, 그냥 select_one("a")로 진행해야 한다.
        title = anchor['aria-label']
        link = anchor['href']
        company= job.find("span", class_="companyName")
        region = job.find("div", class_="companyLocation")
        job_data = {
        'link':f"https://kr.indeed.com{link}", # 절대경로가 아니라, 상대경로이다. f는 format의 상대경로이다.
        'company':company.string,
        'location':region.string,
        'position':title  # aria-label 을 통해 가져 왔으므로,
        }
        results.append(job_data)
        print(results)




