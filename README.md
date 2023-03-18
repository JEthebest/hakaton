После клонирования проекта для запуска используйте следующие команды

'docker compose build'

'docker compose up'

После выполнения этих команд зайдите в Docker контейнер по команде

'docker exec -it bash'

После входа в контейнер пропишите следующие команды

'python manage.py makemigrations'

'python manage.py migrate'

'python manage.py import_air --path tort/scripts/air_list.csv' Для заполнения городов

'python manage.py import_company --path tort/scripts/company_list.csv' Для заполнения продуктов

Для входа в админку создать юзера по команде

'python manage.py cratesuperuser'
