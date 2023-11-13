import psycopg2

class DBManager:
    """Класс получения информации из БД"""
    def __init__(self, cursor):
        self.cursor = cursor

    def get_companies_and_vacancies_count(self):
        """Получение списка компаний и кол-ва вакансий"""
        self.cursor.execute("SELECT employer_name, COUNT(*) AS vacancies_count "
                            "FROM vacancies "
                            "INNER JOIN employers USING(employer_id) "
                            "GROUP BY employer_name "
                            "ORDER BY vacancies_count DESC")

        return self.cursor.fetchall()


    def get_all_vacancies(self):
        """Получение списка всех вакансий"""
        self.cursor.execute("SELECT employer_name, vacancy_name, vacancy_salary_from, "
                            "vacancy_salary_to, vacancy_url "
                            "FROM vacancies "
                            "INNER JOIN employers USING(employer_id)")

        return self.cursor.fetchall()

    def get_avg_salary(self):
        """Получение средней зарплаты по всем найденным вакансиям"""
        self.cursor.execute("SELECT AVG(vacancy_salary_to) FROM vacancies")

        return self.cursor.fetchall()


    def get_vacancies_with_higher_salary(self):
        """
        Получение списка вакансий с ЗП больше чем средняя "от" и средняя "до" по всем вакансиям
        """
        self.cursor.execute("SELECT vacancy_id, vacancy_name, employer_id, "
                            "vacancy_salary_to, vacancy_url FROM vacancies "
                            "INNER JOIN employers USING(employer_id) "
                            "WHERE vacancy_name IS NOT NULL "
                            "GROUP BY vacancy_id, vacancy_name, employer_id, "
                            "vacancy_salary_to, vacancy_url "
                            "HAVING vacancy_salary_to > (SELECT AVG(vacancy_salary_to) "
                            "FROM vacancies)")

        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получение списка вакансий по ключевому слову"""
        self.cursor.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{keyword}%'")
        return self.cursor.fetchall()

