import psycopg2
from configparser import ConfigParser

vacancies_id_dict = {
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

def config(filename, section):
    """Получение параметров БД из файла конфигурации"""
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db

def create_db(params, db_name) -> None:
     """Создание БД и таблиц"""
     print("Создание базы данных")

     conn = psycopg2.connect(dbname='postgres', **params)
     conn.autocommit = True
     cur = conn.cursor()

     cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
     cur.execute(f"CREATE DATABASE {db_name};")

     cur.close()
     conn.close()

     print("Создание базы данных завершено!")

     #  создание таблиц
     print("Создание таблиц с работодателями и вакансиями")
     conn = psycopg2.connect(dbname=db_name, **params)
     with conn.cursor() as cur:
         cur.execute("""
             CREATE TABLE employers (
                employer_id int PRIMARY KEY NOT NULL,
                employer_name varchar(50)
             )
         """)

     with conn.cursor() as cur:
         cur.execute("""
             CREATE TABLE vacancies (
                vacancy_id int PRIMARY KEY NOT NULL,
                employer_id int REFERENCES employers(employer_id) NOT NULL,
                vacancy_name varchar(100) NOT NULL,
                vacancy_salary_from int NOT NULL,
                vacancy_salary_to int NOT NULL,
                vacancy_url text
            )
         """)

     conn.commit()
     conn.close()

     print("Создание таблиц завершено!")

def save_data_to_database(vacancies_list, db_name, params ):
    '''Заполнение таблиц'''

    conn = psycopg2.connect(dbname=db_name, **params) # создание подключения к БД
    with conn.cursor() as cur:
        for k_name in vacancies_id_dict:
            cur.execute(f"INSERT INTO employers VALUES (%s, %s)",
                           (int(vacancies_id_dict[k_name]), k_name))

        for item in vacancies_list:
            cur.execute(f"INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)",
                           (int(item['id']), int(item['employer']['id']), item['name'],
                            item['salary']['from'], item['salary']['to'], item['alternate_url']))

    conn.commit()
    conn.close()

    print("Таблицы заполнены!")