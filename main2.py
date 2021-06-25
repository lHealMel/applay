from bs4 import BeautifulSoup as bs
import requests


def my_function():
    word = input("단어를 입력하세요: ")
    url = "https://www.10000recipe.com/recipe/list.html?q=" + word

    response = requests.get(url)
    html = response.text
    soup = bs(html, 'html.parser')

    title_list = []
    buyer_list = []
    link_list = []

    # 제목 추출
    my_recipe_title = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all("div", {'class': 'common_sp_caption_tit line2'})
    for recipe in my_recipe_title:
        # Tag안의 텍스트
        title_list.append(recipe.text)

    # 조회수 추출
    my_recipe_buyer = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all('span', {'class': 'common_sp_caption_buyer'})
    for recipe in my_recipe_buyer:
        # Tag안의 텍스트
        buyer_list.append(recipe.text)

    # 링크 추출
    my_recipe_link = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all('a', {'class': 'common_sp_link'})
    for recipe in my_recipe_link:
        # Tag안의 href
        link_list.append(recipe['href'])
        # href는 앞부분(https://www.10000recipe.com)이 생략되어 나옴

    print(title_list)
    print(link_list)
    print(buyer_list)


if __name__ == '__main__':
    my_function()


