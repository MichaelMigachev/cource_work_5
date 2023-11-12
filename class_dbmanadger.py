import psycopg2

class DBManager:
    """Класс получения информации из БД"""
    def __init__(self, cursor):
        self.cursor = cursor

    def get_companies_and_vacancies_count(self):
        """Получение списка компаний и кол-ва вакансий"""
        pass

    def get_all_vacancies(self):
        """Получение списка всех вакансий"""
        pass
    def get_avg_salary(self):
        """Получение средней зарплаты по всем найденным вакансиям"""
        pass


    def get_vacancies_with_higher_salary(self):
        """
        Получение списка вакансий с ЗП больше чем средняя "от" и средняя "до" по всем вакансиям
        """
        pass

    def get_vacancies_with_keyword(self, keyword):
        """Получение списка вакансий по ключевому слову"""
        pass