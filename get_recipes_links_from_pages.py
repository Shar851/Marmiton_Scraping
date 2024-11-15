from bs4 import BeautifulSoup
import requests


def get_recipes_links_from_pages(page_link:str)->list:
    recipes_link=[]
    response = requests.get(page_link)
    if response.status_code != 200:
        print("ERROR - Status code")
    else:
        content_html = response.text
        soup = BeautifulSoup(content_html, "html.parser")
        all_tags_a=soup.find_all("a",class_="recipe-card-link")
        for tag_a in all_tags_a:
            link = tag_a.get("href")
            recipes_link.append(link)
    return recipes_link


