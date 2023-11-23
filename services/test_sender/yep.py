import logging

from pyrogram import enums, Client
from environs import Env
from datetime import datetime
from emoji import emojize
from random import randint
from time import sleep

from data.emojies import Emo
from data.some_vip_data.tags_format import *
from services.test_sender.some_text_to_send import txt

env = Env()
env.read_env()
id_ifill = env("id_ifill")
hash_ifill = env("hash_ifill")
my_id = env("my_id")
my_hash = env("my_hash")
ira_id = env("ira_id")
ira_hash = env("ira_hash")
# file_to_who_send = '/home/i/MyPros/F/All_utils_project/services/tg_parser_group/lst_TOSEND_PRIGLOS.txt'
ids_set = set()
# logging.basicConfig(level=logging.DEBUG)

# to_who_send = env('ira_tg_username')
to_who_send = 'Ihdjjd'

ids_set.add(to_who_send)


def emoj(smile):
	return emojize(smile, variant="emoji_type")


text = (
	f'Приветствую! Меня зовут Филатова Ирина, я тренер Лингвистики, соавтор одноименной книги)) {emoj(Emo.hugs)}\n\n'
	f'Лингвистика - очень объёмный и сложный тренинг, и я его бесконечно люблю {emoj(Emo.heart)}\n\n'
	f'{text_to_spoiler("При этом, тема комплиментов раскрыта в нём, на мой взгляд, не полностью")} {emoj(Emo.omg_cat_face)}\n'
	f'А ведь это один из важнейших навыков для установления раппорта {emoj(Emo.red_exclamation)}\n\n'
	f'30 ноября стартует мой авторский онлайн курс "Доброе слово для кошки" {emoj(Emo.hand_over_mouth)}\n\n'
	f'На нём мы разберём не только, что говорить и как говорить, '
	f'но и психо-физиологические основы этого процесса {emoj(Emo.nerd_face)}\n\n'
	f'Комплименты в зависимости от цели (для разного уровня раппорта)\n\n'
	f'2 лекционных вебинара в неделю, и 3 встречи обратной связи.'
	f' Запись будет, будет чат, в котором я так же буду отвечать на вопросы {emoj(Emo.big_smile)}\n\n'
	f'Записаться, ознакомиться подробнее тут https://fillatova.ru\n'
	f'Price = 7000{Emo.ruble}\n\n'
	f'Там есть даже подробный mindmap, где возле вкладок есть цифры - сколько ещё подвкладок {emoj(Emo.explosive_head)}\n\n'
	f'Присоединяйся! Давай вместе создавать новые горизонты мышления! {emoj(Emo.sunglasses)}')


def sender():
	logging.basicConfig(level=logging.INFO)
	for i in ids_set:  # Перебор всех id в из списка
		with Client('my_account', my_id, my_hash) as app:
			text = txt
			app.send_message(i, text=text)  # Отправляем сообщение


sender()
