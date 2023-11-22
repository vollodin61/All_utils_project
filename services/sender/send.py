import logging
from typing import List

from pyrogram import Client
from environs import Env
from datetime import datetime
from emoji import emojize
from random import randint
from time import sleep

from data.emojies import Emo

env = Env()
env.read_env()
id_ifill = env("id_ifill")
hash_ifill = env("hash_ifill")
my_id = env("my_id")
my_hash = env("my_hash")
my_tg_id = env("my_tg_id")
ira_id = env("ira_id")
ira_hash = env("ira_hash")
file_to_who_send = '/home/i/MyPros/F/All_utils_project/services/tg_parser_group/lst_TOSEND_PRIGLOS.txt'
ids_set = set()
new_ids_list = list()


def emoj(smile):
	return emojize(smile, variant="emoji_type")


text = (
	f'Приветствую! Меня зовут Филатова Ирина, я тренер Лингвистики, соавтор одноименной книги)) {emoj(Emo.hugs)}\n\n'
	f'Лингвистика - очень объёмный и сложный тренинг, и я его бесконечно люблю {emoj(Emo.heart)}\n\n'
	f'При этом, тема комплиментов раскрыта в нём, на мой взгляд, не полностью {emoj(Emo.omg_cat_face)}\n'
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


def send_for_who(for_who, remain):
	with Client('my_account', ira_id, ira_hash) as app:
		app.send_message(for_who, text=f'Осталось {remain} циклов')


def make_list_for_send(lst: List):
	with open(file_to_who_send, "r", encoding="utf-8") as f:
		id_list = f.readlines()
		{ids_set.add(i[:-1]) for i in id_list}
		lst = list(ju for ju in ids_set)
	return lst


lst_for_send = make_list_for_send(new_ids_list)


def sender(n_lst: List):
	for i in n_lst:  # Перебор всех id в из списка
		with (Client('my_account', ira_id, ira_hash) as app,
				open('sended.txt', 'a+', encoding='utf-8') as sended,
				open('sender_log.txt', 'a+', encoding='utf-8') as log):
			try:
				app.send_message(i, text=text)  # Отправляем сообщение
				sleep(randint(2, 4))
				sended.write(str(i) + "\n")
				n_lst.remove(i)
			except Exception as err:
				log.write(f'{i} не получил сообщение в {datetime.now().strftime("%Y:%b:%d %H:%M:%S")} по причине: {err}\n')
				n_lst.remove(i)


def main():
	logging.basicConfig(level=logging.INFO)
	total = 0  # всего ids считает скольким уже сделана попытка отправить
	temp_count = 0  # временная считалка, чтоб не спамить сильно
	loop_count = 0  # считает какой цикл отправки сейчас идёт
	total_loops = len(ids_set) / 11  # сколько всего циклов
	loops_remain = total_loops - loop_count  # сколько циклов осталось
	while total < len(ids_set):  # пока total меньше числа id в изначальном ids_set будет отправлять
		if temp_count < 10:
			if "10:00:00" < datetime.now().time().strftime("%H:%M:%S") < "21:00:00":
				temp_count += 1
				total += 1
				sender(lst_for_send)  # список кому отправить в этот цикл
				sleep(randint(3, 5))
		else:
			temp_count = 0
			loop_count += 1
			send_for_who(my_tg_id, loops_remain)
			sleep(randint(2521, 5442))
