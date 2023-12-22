[![Build Status](https://app.travis-ci.com/kpdvstu/PTLab2.svg?branch=master)](https://app.travis-ci.com/kpdvstu/PTLab2)
# Лабораторная 2 по дисциплине "Технологии программирования"

Цели работы:
- Познакомиться c моделью MVC, ее сущностью и основными фреймворками на ее основе.
- Разобраться с сущностями «модель», «контроллер», «представление», их функциональным
назначением.

Вариант № 9

Тема: Магазин канцелярских товаров
Задача:
Покупателю должна быть предоставлена скидка в 10% на любой
товар в его день рождения.


После клонирования репозитория, установки postgres и предварительной настройки проекта выполним все миграции в базу данных:

'''

PS E:\PTLab2> python manage.py migrate     
WARNING:root:No DATABASE_URL environment variable set, and so no databases setup
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, shop
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying shop.0001_initial... OK

'''

После чего загрузим данные в базу из файла products.yaml с помощью команды python manage.py loaddata. Затем запустим тесты и убедимся, что все работает без ошибок.

Добавим в базу товары в соответствии с темой:
'''
- model: shop.product
  pk: 1
  fields:
    name: Набор карандашей
    price: 120
- model: shop.product
  pk: 2
  fields:
    name: Тетрадка 48 листов
    price: 150
- model: shop.product
  pk: 3
  fields:
    name: Ластик
    price: 30
'''

В класс PurchaseCreate добавим дополнительный функционал, реализующий поставленную задачу:

'''
def form_valid(self, form):
        self.object = form.save()
        info = ''
        if (self.object.date == datetime.now()):
            info = 'В честь вашего дня рождения, вам будет предоставлена скидка 10%!'
        return HttpResponse(f'Спасибо за покупку, {self.object.person}! {info}')
'''

Выводы: В ходе выполения работы было разработано приложение, отвечающее требованиям исходной задачи.