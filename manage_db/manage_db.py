import psycopg2
import time
from dateutil import parser
time.sleep(5)
connection = psycopg2.connect(dbname='postgres', user='postgres',\
                 password='postgres', host='localhost', port=5432)
cursor = connection.cursor()
cursor.execute("CREATE TABLE if not exists test (id serial PRIMARY KEY, ip varchar(50), time  timestamp, request varchar(5), error_code integer, system_info varchar(150));")
with open('/mnt/nginx_logs.txt') as f:
    content = f.readlines()
for i in content:
        ip_adress, _, _, string = i.strip().split(maxsplit=3)
        datetime, string = string.split(sep='] ')
        datetime = datetime[1:]
        date_time = parser.parse(datetime, fuzzy=True)
        request, string = string.split(sep='" ',maxsplit=1)
        request, _ = request[1:].split(maxsplit=1)
        error_code, _, _, system_info = string.split(maxsplit=3)
        system_info = system_info[1:-1]
        insert = f"INSERT INTO test (ip,time,request,error_code,system_info) VALUES ('{ip_adress}', '{date_time}', '{request}', {error_code}, '{system_info}')"
        cursor.execute(insert)
connection.commit()
cursor.execute('SELECT ip, time, request, error_code, system_info FROM test')
records = cursor.fetchall()
print('Let us see the top 5 values in the our own database')
for i in records[:5]:
        print(i)
try:
        cursor.close()
        connection.close()
except:
        connection.close()