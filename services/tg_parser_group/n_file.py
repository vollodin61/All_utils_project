import json
import logging
import re

from pyrogram import Client
from environs import Env


# "Лингвистика Общий чат" : -1253838063
# 846106824 неугодный id

# ids = 'Fil_group.json' # Откуда брать username и id
group_ids = '/home/i/MyPros/F/All_utils_project/services/tg_parser_group/lingva_groups.json'

tmp_list = 'tmp_list.txt'  # Временный тхт записывать username
noname_tmp_list = 'tmp_noname_list.txt'  # Временный тхт записывать у кого нет username
clear_tmp_list = 'clear_tmp_list.txt'  # тхт очищенный по всяким фильтрам типа "плохиши" и "уже проходили"
bad_boys = 'bad_boys.txt'  # "плохиши"
old_boys = '/home/i/MyPros/F/All_utils_project/data/cat_users_07112023.txt'  # "уже проходили"
env = Env()
env.read_env()
ira_id = env('ira_id')
ira_hash = env('ira_hash')
with open(group_ids, 'r') as f:
	ids = json.loads(f.read())


def parse(ids: str, tmp_list: str, noname_tmp_list: str):
	client = Client('from_ira_getter', api_id=ira_id, api_hash=ira_hash)
	client.start()
	logging.basicConfig(level=logging.INFO)

	for v in ids.values():
		lst = client.get_chat_members(v)
		for i in lst:
			with open(tmp_list, 'a+', encoding='utf-8') as f:
				if i.user.username and not i.user.is_bot:
					f.write(f"{i.user.username}\n")
				else:
					f.write(f"{i.user.id}\n")
					with open(noname_tmp_list, 'a+', encoding='utf-8') as noname:
						noname.write(f"{i.user.id} -- {i.user.first_name} {i.user.last_name} tel {i.user.phone_number}\n")
	client.stop()


def cleanup(tmp_lst: str, clear_tmp: str, bad_b: str, dont_send: str):
	with (open(tmp_lst, 'r', encoding='utf-8') as old_tmp,
		  open(clear_tmp, 'w+', encoding='utf-8') as clear,
		  open(bad_b, 'r', encoding='utf-8') as bads,
		  open(dont_send, 'r', encoding='utf-8') as cats):

		dct = {u[:-1] for u in cats.readlines()}  # получаем сет кто был на Кошке
		print(dct)
		for k in bads.readlines():  # Добавляем всех из списка плохишей в сет кому не будем отправлять
			username = re.findall(pattern=r"[A-Za-z]\S+", string=k)
			# tel = re.match(pattern=r"/d+", string=k)
			try:
				dct.add(username[0])
				# print(username[0])
			except Exception:
				# print(k[:-1])
				pass
		# print(dct)
		n_dct = {n[:-1] for n in old_tmp.readlines()}  # Другой словарь из тех, кто есть в файле tmp(old_tmp)
		n_dct.difference_update(dct)  # Вычитаем из tmp(old_tmp) неугодных для отправки сообщения
		for i in n_dct:  # Перебираем
			# if not i in dct:  # Если i из нового словаря нет в старом, то записываем в файл clear_tmp
			clear.write(i + "\n")
		# (clear.write(i + '\n') for i in n_dct)  # записываем всех в новый файл
		# print(n_dct)
	with open(tmp_lst, 'wb'):
		pass

def main():
	parse(ids=ids, noname_tmp_list=noname_tmp_list, tmp_list=tmp_list)
	cleanup(tmp_lst=tmp_list, clear_tmp=clear_tmp_list, bad_b=bad_boys, dont_send=old_boys)


if __name__ == '__main__':
	main()
