from selenium import webdriver
from bs4 import BeautifulSoup as bs

# selenium 안쓰고 그냥 urllib쓰는 버전도 만들어보기

def my_function():
    word = input("단어를 입력하세요: ")
    browser = webdriver.Chrome()
    url = "https://www.10000recipe.com/recipe/list.html?q=" + word
    browser.get(url)

    soup = bs(browser.page_source, 'html.parser')
    
    # 제목 추출
    my_recipe_title = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all("div", {'class': 'common_sp_caption_tit line2'})
    for recipe in my_recipe_title:
        # Tag안의 텍스트
        print(recipe.text)

    # 조회수 추출
    my_recipe_buyer = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all('span', {'class': 'common_sp_caption_buyer'})
    for recipe in my_recipe_buyer:
        # Tag안의 텍스트
        print(recipe.text)

    # 링크 추출
    my_recipe_link = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all('a', {'class': 'common_sp_link'})
    for recipe in my_recipe_link:
        # Tag안의 href
        print(recipe['href'])
        # href는 앞부분(https://www.10000recipe.com)이 생략되어 나옴

if __name__ == '__main__':
    my_function()

