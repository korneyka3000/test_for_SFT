# Тестовое задание

---

>python == 3.10

>Django == 4.2.1

`Для запуска надо:`

- Склонировать репозиторий
    ```bash
    git clone https://github.com/korneyka3000/test_for_SFT.git
    ```
- Перейти в папку проекта
    ```bash
    cd sft_project
    ```
- Создать виртуальное окружение
    ```bash
    python3 -m venv venv
    ```
- Активировать виртуальное окружение для Linux
    ```bash
    . venv/bin/activate
    ```
  Или для windows
    ```bash
    venv\Scripts\activate  
    ```
- Установить зависимости
    ```bash
    pip install -r requirements.txt
    ```
- Создать миграции для БД:
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```
- Заполнить БД данными:
    ```bash
    python manage.py loaddata > credit_app_db_dump.json
    ```
- Запустить проект и перейти по ссылке в терминале:
    ```bash
    python manage.py runserver
    ```

