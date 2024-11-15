def get_all_pages_links(total_pages:int)->list:
    recipes_links = []
    base_url="https://www.marmiton.org/recettes/index/categorie/dessert/"
    for page in range (1,total_pages+1):
        url=base_url + str(page)
        recipes_links.append(url)
    return recipes_links
