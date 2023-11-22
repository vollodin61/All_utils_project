from pyrogram import Client
from time import sleep
from datetime import datetime


# Этот бот вытаскивает данные о учачастниках чата/группы https://t.me/parsetgbot
_id_ = '26315421'
_hash_ = '6381a688ef53e5f6dfc29bbc29bc9381'
# id_list = [  # Список кому отправляем
#     6327890637, 585791811, 455393227, 358169459,
#     724173761, 5261985728, 412342295, 1580070365, 144370626,
#     74890341, 281032977, 208814680, 355238842, 326057616,
#     218961093, 135294168, 498239117, 1889268026, 107833444,
#     222374754, 330332417, 817907280, 222593486,
# ]

with open("data/users.txt", "r", encoding="utf-8") as f:  # TODO тут неправильно указан адрес файла с пользователями
    id_list = f.readlines()



def reminds():  # Можно сделать так, чтоб вызывать этого бота дистанционно, отправляя ему список с id
    """Функция от моего имени отправляет напоминания"""
    count = 0
    now_moment = datetime.now().strftime("%Y:%b:%d %H:%M:%S")
    while count < 45:
        for i in id_list:  # Перебор всех id в из списка стр 7
            try:
                with Client('my_account', _id_, _hash_) as app:  # Логинимся в телеге
                    app.send_message(i[:-1], 'Время для быстрого и легкого комплимента!)')  # Отправляем сообщение
            except Exception as err:
                with Client('my_account', _id_, _hash_) as app:
                    app.send_message('me', f'{i} не получил сообщение похвалить себя') # Сообщение самому себе кто не получил
                with open('log.txt', 'a+', encoding='utf-8') as f:  # Запись в лог, кто и во сколько не получил
                    f.write(f'\n{i} не получил сообщение в {datetime.now().strftime("%Y:%b:%d %H:%M:%S")} по причине: {err}')

        print(f'Цикл №{count + 1} завершен в {datetime.now().strftime("%Y:%b:%d %H:%M:%S")}')  # Вот тут по дефолту стоит 0 вместо 18
        count += 1
        sleep(600)




def sender_hashtags():
    """Функция отправляет Боту Геннадию хэштеги"""
    _id = 979328150
    tags_list = []

    for tag in tags_list:
        try:
            with Client('my_account', _id_, _hash_) as app:
                app.send_message(_id, tag)
        except:
            app.send_message('me', 'Бот Геннадий не получил сообщение')


if __name__ == "__main__":
    reminds()