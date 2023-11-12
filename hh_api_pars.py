import requests
from pprint import pprint

# словарь с данными о работадателях
empl_items = {
        "СБЕР": "3529",
        "Газпром нефть": "39305",
        "2ГИС": "64174",
        "Центр винного туризма Абрау Дюрсо": "2240534",
        "VERTEX": "1800569",
        "КАМАЗ": "52951",
        "ФосАгро": "2227671",
        "Россети Ленэнерго": "203987",
        "Skyeng": "1122462",
        "Битрикс24": "129044"
    }

# список id работодателей
employees_id_list = ["3529", "39305", "64174", "2240534", "1800569",
                         "52951", "2227671", "203987", "1122462", "129044"]


def get_vacancies():
    """Получение всех вакансий компаний"""
    vacancies_list = []
    hh_vac_url = 'https://api.hh.ru/vacancies'

    for num in range(len(employees_id_list)):
        params = {
            "employer_id": employees_id_list[num],
            "per_page": 100,
            "only_with_salary": True
        }
        response = requests.get(hh_vac_url, params=params)
        vacancies = response.json()
        for item in vacancies["items"]:
                if item["salary"]["from"] and item["salary"]["to"]:
                    vacancies_list.append(item)

    return vacancies_list

# vacancies_list = get_vacancies()
# pprint(vacancies_list[0])
