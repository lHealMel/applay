from bs4 import BeautifulSoup as bs
import requests


def main():
    word = input("단어를 입력하세요: ")
    my_function_man(word)
    print("크롤링 1 완료")
    my_function_hae(word)
    print("크롤링 2 완료")
    print("크롤링 전체 완료")


# 만개의 레시피에서 크롤링
def my_function_man(word):
    url = "https://www.10000recipe.com/recipe/list.html?q=" + word

    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    soup = bs(html, 'html.parser')

    title_list = []
    buyer_list = []
    link_list = []
    img_list = []

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

    # 이미지지 추출
    my_recipe_img = soup.find('ul', {'class': 'common_sp_list_ul ea4'}).find_all('img')
    for recipe in my_recipe_img:
        # Tag안의 src
        img_list.append(recipe['src'])

    title_list = [string + "\n" for string in title_list]
    link_list = [string + "\n" for string in link_list]
    buyer_list = [string + "\n" for string in buyer_list]

    r_file = open("테스트.txt", "a", encoding='utf-8')
    for i in range(len(title_list)):
        r_file.write(title_list[i])
        r_file.write(link_list[i])
        r_file.write(buyer_list[i])
        r_file.write('\n')
    r_file.close()


# 해먹에서 크롤링
def my_function_hae(word):
    url = "https://haemukja.com/recipes?utf8=%E2%9C%93&sort=rlv&name=" + word

    response = requests.get(url)
    html = response.text
    soup = bs(html, 'html.parser')

    title_list2 = []
    buyer_list2 = []
    link_list2 = []
    img_list2 = []

    # 제목 추출
    my_recipe_title = soup.find('ul', {'class': 'lst_recipe'}).select('a > strong')
    for recipe in my_recipe_title:
        # Tag안의 텍스트
        title_list2.append(recipe.text)

    # 조회수 추출
    my_recipe_buyer = soup.find('ul', {'class': 'lst_recipe'}).find_all('button', {'class': 'btn_like'})
    for recipe in my_recipe_buyer:
        # Tag안의 텍스트
        buyer_list2.append(recipe.text)

    # 링크 추출
    my_recipe_link = soup.find('ul', {'class': 'lst_recipe'}).select('p>a')
    for recipe in my_recipe_link:
        # Tag안의 href
        link_list2.append(recipe['href'])
        # href는 앞부분(https://www.10000recipe.com)이 생략되어 나옴

    # 이미지지 추출
    my_recipe_img = soup.find('ul', {'class': 'lst_recipe'}).find_all('img')
    for recipe in my_recipe_img:
        # Tag안의 src
        img_list2.append(recipe['src'])

    title_list2 = [string + "\n" for string in title_list2]
    link_list2 = [string + "\n" for string in link_list2]
    buyer_list2 = [string + "\n" for string in buyer_list2]

    r_file = open("테스트2.txt", "a", encoding='utf-8')
    for i in range(len(title_list2)):
        r_file.write(title_list2[i])
        r_file.write(link_list2[i])
        r_file.write(buyer_list2[i])
        r_file.write('\n')
    r_file.close()


if __name__ == '__main__':
    main()
