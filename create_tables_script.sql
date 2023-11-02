------ удаляем таблицы если они есть
---DROP TABLE IF EXISTS employers;
---DROP TABLE IF EXISTS vacancies;

--- выполните в pgAdmin 4

--- создание базы данных
CREATE DATABASE cw_5_bd

--- Создание таблицы работодателей
---
CREATE TABLE employers (
    employer_id int PRIMARY KEY NOT NULL,
    employer_name varchar(50)
);

---
--- Создание таблицы вакансий
---

CREATE TABLE vacancies (
    vacancy_id int PRIMARY KEY NOT NULL,
    employer_id int REFERENCES employers(employer_id) NOT NULL,
    vacancy_name varchar(100) NOT NULL,
    vacancy_salary_from int NOT NULL,
    vacancy_salary_to int NOT NULL,
    vacancy_url text
);