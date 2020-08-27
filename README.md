
      1. Установим неоходимые расширения. 

Для этого создадим виртуальное окружение:
	python3 -m venv env

Активвируем:
	source env/bin/activate
	
Скачиваем тестовое задание: 
	git clone 'сюда вставить ссылку на репозиторий'

Переходим в папку с проектом (директория с manage.py) и устанавливаем зависимоти:
	pip3 install -r requirements.txt
 
      2. Запустим сервер.

При первом запуске необходимо выполнить миграции:
	python3 manage.py makemigrations
	python3 manage.py migrate

Запускаем:
	python 3 manage.py runserver 9000

Переходим на страничку: 
	http://localhost:9000/
  
Выбираем необходимый API и проверяем:
  Например http://localhost:9000/users/add (в поле ввода необходимо ввесни нужный request и нажать post)

При необходимости входа в административную панель:
	python3 manage.py createsuperuser (Заполнить данные и ввести по адресу http://localhost:9000/admin/) 
