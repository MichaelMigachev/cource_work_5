import psycopg2
from hh_api_pars import get_vacancies
from utils_bd import config, create_db,save_data_to_database


db_name = 'cw_5_bd'
params = config('database.ini', 'postgresql')  # Создание переменной параметров доступа к БД


# print (params)

vacancies_list = get_vacancies()
# pprint(vacancies_list[0])

# создание базы данных
create_db(params, db_name)

# Заполнение таблиц
save_data_to_database(vacancies_list, db_name, params )
