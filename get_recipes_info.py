from bs4 import BeautifulSoup
import requests
from convert_to_min import convert_to_min

def get_recipes_info(recipe_link:str)->dict:
    response=requests.get(recipe_link)
    content_html=response.text
    soup=BeautifulSoup(content_html,"html.parser")
    recipe_info={}
    if soup.find("h1") != None:
        recipe_info["name"]=soup.find("h1").text.strip()
    else:
        return None

    recipe_info["recipe_link"]= recipe_link

    recipe_info["ingredients"]=[
        ingredient.text.strip() for ingredient in soup.find_all("span", class_="ingredient-name")
    ]
    
    breadcrumb_links=soup.find("p", class_="af-bread-crumb").find_all("a")
    if len(breadcrumb_links)>3:
        recipe_info["category"]= breadcrumb_links[3].get_text(strip=True)
    else:
        recipe_info["category"]= "Uncategorized dessert"

    prep_time_text = soup.find("i", class_="icon icon-timer1").find_next("span").get_text(strip=True)
    print(recipe_link)
    recipe_info["prep-time"]=convert_to_min(prep_time_text)
    
    div_tag2=soup.find_all("div", class_="recipe-primary__item")
    for div in div_tag2:
        text=div.text.strip()
    recipe_info["budget"]= text

    div_tag3=soup.find("div",class_="recipe-header__comment")
    review_count_text=div_tag3.text.strip()
    digits = review_count_text.split()[0]
    recipe_info["review count"] = int(digits) 

    div_tag4=soup.find("div",class_="recipe-header__rating")
    rating_text=div_tag4.text.strip()
    recipe_info["rating"]= float(rating_text.split("/")[0])

    div_tag5=soup.find_all("div", class_="recipe-primary__item")
    for div in div_tag5:
        icon = div.find("i", class_="icon icon-difficulty")
        if icon:
            span_tag = div.find("span")
            if span_tag:
                recipe_info["difficulty"]=span_tag.text.strip()
            break

    div_tag6=soup.find_all("div", class_="recipe-step-list__container")
    recipe_info["steps_count"]=len(div_tag6)

    return recipe_info
