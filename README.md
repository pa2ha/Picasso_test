## Клонировать проект
```
git clone git@github.com:pa2ha/Picasso_test.git
cd Picasso_test
```

Cоздать файл .env в корне проекта и заполнить его
```
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=menu
POSTGRES_USER=fastapi
POSTGRES_PASSWORD=mypass
```
### запустить докер-компоуз
```
docker-compose up
```

# Как запустить Тесты

### После того как все контейнеры запустятся, открыть дополнительный терминал и выполнить в нём команду
```
docker exec -it picasso_test-backend-1 python ./Picasso/manage.py test main.tests
```
Автоматически создастся тестовая база и запустятся тесты


# Как запустить API


### После того как все контейнеры запустятся, открыть дополнительный терминал и выполнить в нём команду


```
docker exec -it picasso_test-backend-1 python ./Picasso/manage.py migrate
```
После этого будет доступен API по адресу:
```
http://127.0.0.1:8000/api/
```

## Опишите, как изменится архитектура, если мы ожидаем большую нагрузку

Можно развернуть несколько экземпляров API сервера и распределите трафик между ними с помощью балансировки нагрузки. Это позволит увеличить пропускную способность и обеспечить отказоустойчивость.



Можно использовать кэширование для хранения результатов запросов или вычислений, которые могут быть повторно использованы. Это поможет сократить время ответа и уменьшить нагрузку на сервер.

## Попробуйте оценить, какую нагрузку в RPS сможет выдержать ваш сервис

Из-за того что у нас нет конкретной обработки получаемых файлов в функции, то сервис может выдержать относительно большую нагрузку.
Производительность сервиса будет ограничена прежде всего пропускной способностью сервера и базы данных и варьироваться(по моему мнению)
от 10 до 100 RPS
