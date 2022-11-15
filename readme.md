1. Создать виртуальное окружение
`python3.10 -m venv venv`

2. Активировать
`. venv/bin/activate`

3. Обновить pip
`pip install -U pip`

4. Скачать библиотеки
`pip install -r requirements.txt`

5. Создать папку для логов (если её нет)
`mkdir logs`

6. Создать env.sh и дать права на запуск
`touch env.sh && chmod +x env.sh`

7. Добавить переменные окружения
```bash
API_URL - Ссылка на Backend в локальной сети (http://127.0.0.1:8000)
API_TOKEN - Токен администратора
YOOKASSA_ID - Айди приложения YooKassa
YOOKASSA_TOKEN - Токен приложения YooKassa
```

8. Запустить env.sh
`. ./env.sh`

9. Запустить uvicorn
`uvicorn core:application --port 8080 --log-config logging.conf`
