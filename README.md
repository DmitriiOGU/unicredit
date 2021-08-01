Комманда для старта: docker-compose -f docker-compose.yml up --build
Для запуска должен быть свободен порт 5432 и установлен доккер. Для развертывания базы используется Docker-контейнер

Сервис-1. База данных. Сервис запускается, ожидает входящих соединений на своем порту. 

Сервис-2. Контейнер со скриптом для наполнения базы. Сервис запускается, подключается по порту к базе данных и заполняет базу набором данных. Набор данных скачивается через утилиту curl. 
Сервис-2 стартует после старта сервиса-1.


Подразумеваю, что данная задача могла решаться ещё одним способом, с помощью разворачивания физического экземпляра БД или же также контейнера, 
но скрипт можно было запустить не в Docker-контейнере, в таком случае можно было использовать следующую конструкцию для загрузки без curl:

КОД:


	import requests
	import io
	url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
	download = requests.get(url).content
	with open(io.StringIO(download.decode('utf-8'))) as f:
		content = f.readlines()
