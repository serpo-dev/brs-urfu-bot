import re
from bs4 import BeautifulSoup as bs4
import json

def formatter(string, index=None):
    if index != None:
        print(index, "!!!!!!!!!!!!!!")
    new_string = string.replace("—", " — ")
    new_string = new_string.replace("×", " × ")
    new_string = new_string.replace("=", " = ")
    new_string = new_string.replace("/", " / ")
    new_string = new_string.replace("из", " из ")

    pattern_html_tags = r"(\<[^>]+>)|([\t]+)|([\n\r]+)"
    new_string = re.sub(pattern_html_tags, "", new_string)

    pattern_one_space = r"([\s]{2,})"
    new_string = re.sub(pattern_one_space, " ", new_string)

    pattern_word_space_number = r"(\d)([A-Za-zА-Яа-я])"
    repl_word_space_number = r"\1 \2"
    new_string = re.sub(pattern_word_space_number, repl_word_space_number, new_string)
    pattern_word_space_number = r"([A-Za-zА-Яа-я])(\d)"
    repl_word_space_number = r"\1 \2"
    new_string = re.sub(pattern_word_space_number, repl_word_space_number, new_string)

    return new_string

def parser(soup):
    all_results = soup.find_all("div", attrs={"class":"all-results"})
    main_result = formatter(all_results[0].find_all("strong", attrs={"class":"brs-h3"})[0].text)

    rating_marks = [formatter(i.text) for i in soup.find_all("p", attrs={"class":"rating-marks"})]

    brs_containers = soup.find_all("div", attrs={"class":"brs-countainer"})[:len(rating_marks)]
    main_brs_slide_pane_conts = [i.find_all("div", attrs={"class":"brs-slide-pane-cont" }) for i in brs_containers]

    main_brs_containers_names_html = [[i.find_all("a", attrs={"class":"brs-slide-pane" }) for i in j] for j in main_brs_slide_pane_conts]
    main_brs_containers_names = [[[formatter(k.text) for k in j][0] for j in i] for i in main_brs_containers_names_html]
    main_brs_containers_items_html = [[i.find_all("div", attrs={"class":"brs-values interim-certification" }) for i in j] for j in main_brs_slide_pane_conts]
    main_brs_containers_items_html_p = [[[k.find_all("p") for k in j] for j in i] for i in main_brs_containers_items_html]
    main_brs_containers_items_p =  [[[[formatter(z.text) for z in k][0] for k in j] for j in i] for i in main_brs_containers_items_html_p]
    
    main_parts = []
    for i, name in enumerate(rating_marks):
        part = {
            "name": name,
            "containers": [{"name": x} for x in main_brs_containers_names[i]],
        }

        for (j, _) in enumerate(main_brs_containers_names[i]):
            part["containers"][j]["items"] =  main_brs_containers_items_p[i][j]

        main_parts.append(part)


    main_result = {"total": main_result, "parts": main_parts}
    return main_result



def get_grades(subjects, session):
    cache_json = []
    url = "https://istudent.urfu.ru/s/http-urfu-ru-ru-students-study-brs/discipline"

    for discipline in subjects:
        discipline_id = discipline[0]
        query = f"?discipline_id={discipline_id}"
        discipline_url = url + query

        result =  session.get(discipline_url)
        html = result.text

        soup = bs4(html, "lxml")
        discipline_json = parser(soup=soup)

        discipline_record = {"id": discipline[0], "title": discipline[1], "grades": discipline_json}

        cache_json.append(discipline_record)

   

    return cache_json