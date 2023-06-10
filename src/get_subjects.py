import re


def get_subjects(session):
    list_url = "https://istudent.urfu.ru/s/http-urfu-ru-ru-students-study-brs"

    response = session.get(url=list_url)
    expires_header = response.headers["Expires"]
    if expires_header == "-1":
        return False, None
    
    pattern = r"\<a\sclass\=\"js\-service\-rating\-link\" id\=\"(\d+)\"\stitle\=\"([A-Za-zА-Яа-я\s1-9]+)\"\>"
    subjects = re.findall(pattern, response.text)
    return True, subjects