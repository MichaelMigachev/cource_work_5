import psycopg2
from hh_api_pars import get_vacancies
from utils_bd import config, create_db,save_data_to_database
from class_dbmanadger import DBManager


db_name = 'cw_5_bd'
params = config('database.ini', 'postgresql')  # Создание переменной параметров доступа к БД
keyword = "Менеджер"

def main():
    vacancies_list = get_vacancies() # Получение всех вакансий компаний

    # создание базы данных
    create_db(params, db_name)

    # Заполнение таблиц
    save_data_to_database(vacancies_list, db_name, params )

    # Получение списка компаний и кол-ва вакансий
    connection = psycopg2.connect(dbname=db_name, **params)
    with connection as conn:
        with conn.cursor() as cur:
            db_manager = DBManager(cur)

            # Пользовательский интерфейс
            while True:
                print("\nВыберете из списка  действий:\n"
                      "1 - Вывести весь список компаний с указанием "
                      "кол-ва найденных вакансий (по убыванию)\n"
                      "2 - Вывести весь список вакансий\n"
                      "3 - Вывести среднюю ЗП по всем вакансиям\n"
                      "4 - Вывести список вакансий у которых ЗП "
                      "выше средней по всем вакансия\n"
                      "5 - Вывести список всех вакансий по ключевому "
                      "слову в названии вакансии\n"
                      "0 - Выйти")
                user_func_input = input("> ")
                if user_func_input == "1":
                    companies = db_manager.get_companies_and_vacancies_count()
                    for company in companies:
                        print(f"Компания: {company[0]}\nКол-во вакансий: {company[1]}\n\n")


                if user_func_input == "2":
                    vacancies = db_manager.get_all_vacancies()
                    for vacancy in vacancies:
                        print(f"Компания: {vacancy[0]}\nВакансия: {vacancy[1]}\n"
                              f"Зарплата от: {vacancy[2]}\nЗарплата до: {vacancy[3]}\n"
                              f"Ссылка: {vacancy[4]}")
                        print()

                if user_func_input == "3":
                    print(f"{round(db_manager.get_avg_salary()[0][0])} руб.")


                if user_func_input == "4":
                    valid_vac = db_manager.get_vacancies_with_higher_salary()
                    for vac in valid_vac:
                        print(f"Вакансия: {vac[1]}\nЗарплата: {vac[3]}\nСсылка: {vac[4]}")
                        print()


                if user_func_input == "5":
                    while True:
                        keyword_input = input("Введите название вакансии, например Менеджер или Водитель, "
                                              "или введите 0 для выхода:\n> ")
                        vac_res_list = db_manager.get_vacancies_with_keyword(keyword_input)
                        if keyword_input == "0":
                            break
                        if len(vac_res_list) == 0:
                            print("С таким словом вакансий нет \nПопробуйте снова!\n")
                        else:
                            for vac in vac_res_list:
                                print(f"Вакансия: {vac[2]}\nЗарплата от: {vac[3]}\n"
                                      f"Зарплата до: {vac[4]}\nСсылка: {vac[5]}")
                                print()
                            break

                if user_func_input == "0":
                    print("Всего хорошего!")
                    break

if __name__ == '__main__':
    main()