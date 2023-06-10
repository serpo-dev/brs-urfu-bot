from bs4 import BeautifulSoup as bs4

from .parser import parser


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