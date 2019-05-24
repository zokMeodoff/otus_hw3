## **Курс Web-разработчик на Python от OTUS**

### **Домашнее задание №3**
Написать свой WSGI веб-фреймворк. 

### Установка

```консоль
$ git clone https://github.com/zokMeodoff/otus_hw3.git
$ cd otus_hw3
$ pip install -r requirements.txt
```

### Запуск

```консоль
$ uwsgi --http :9090 --wsgi-file app.py
```