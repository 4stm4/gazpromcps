#### Развёртывание проекта
##### 1) Создаём виртуальное окружение
`python3.12 -m  venv venv`
##### 2) Активируем виртуальное окружение
`source env/bin/activate`
##### 3) Устанавливаем пакеты
`python3.12 -m pip install -r requirements.txt`
##### 4) В файле settings.py заполняем секцию DATABASE
##### 5) Запускаем миграции
`python3.12 -m manange.py migrate`

#### Запуск проекта
`python3.12 -m manange.py runserver`

##### Запуск тестов
`python3.12 -m coverage run manage.py test`
##### Покрытие тестами
`python3.12 -m coverage report -m`


##### Добавление рейса
`curl --location --request PUT 'http://127.0.0.1:8000/booking/flight_info' \
--header 'Content-Type: application/json' \
--data '{
    "number": "pa_723",
    "aviacompany_name": "Pobeda airlines",
    "seats_cnt": 111,
    "price": 3150,
    "departure": "Челябинск",
    "destination": "Москва",
    "date": "2024-03-28"
}'`

##### Поиск рейса
`curl --location 'http://127.0.0.1:8000/booking/search_flight?departure=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA&destination=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&flight_date=2024-03-28'`

##### Бронирование билетов на рейс
`curl --location 'http://127.0.0.1:8000/booking/order_flight' \
--header 'Content-Type: application/json' \
--data '{"flight_number": "pa_723", "flight_date": "2024-03-28", "seats_cnt": 1}'`