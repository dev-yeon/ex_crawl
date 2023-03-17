

"""
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
    jobs = soup.find_all('section', class_="jobs")
"""
# 5.5 Keyword Arguments
def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")
say_hello("nico",12) #positional = 위치가 중요함.

say_hello(age=12 ,name="nico") # arguments 들의 이름을 정확히 명시하는게 중요해.
# bs.find_all은 엄청나게 많은 arguments를 갖고있기 때문이다.
