import json
import logging
import re

from pyrogram import Client
from pyrogram.types import Message
from environs import Env


# "Лингвистика Общий чат" : -1253838063
def parse():
	env = Env()
	env.read_env()
	ira_id = env('ira_id')
	ira_hash = env('ira_hash')
	with open('tg-groups_for_parsing.json', 'r') as f:
		ids = json.loads(f.read())

	client = Client('from_ira_getter', api_id=ira_id, api_hash=ira_hash)
	client.start()
	logging.basicConfig(level=logging.INFO)

	for v in ids.values():
		lst = client.get_chat_members(v)
		for i in lst:
			with open('tmp_list.txt', 'a+', encoding='utf-8') as f:
				if i.user.username and not i.user.is_bot:
					f.write(f"{i.user.username}\n")
				else:
					f.write(f"{i.user.id}\n")
					with open('tmp_noname_list.txt', 'a+', encoding='utf-8') as noname:
						noname.write(f"{i.user.id} -- {i.user.first_name} {i.user.last_name} tel {i.user.phone_number}\n")
	client.stop()


def cleanup():
	with (open('tmp_list.txt', 'r', encoding='utf-8') as old,
			open('clear_tmp_list.txt', 'a+', encoding='utf-8') as new,
		    open('bad_boys.txt', 'r', encoding='utf-8') as bads,
		    open('/home/i/MyPros/F/All_utils_project/data/cat_users_07112023.txt', 'r', encoding='utf-8') as cats):

		dct = {u[:-1] for u in cats.readlines()}
		print(dct)
		for k in bads.readlines():
			username = re.findall(pattern=r"[A-Za-z]\S+", string=k)
			# tel = re.match(pattern=r"/d+", string=k)
			try:
				dct.add(username[0])
				# print(username[0])
			except Exception as e:
				# print(k[:-1])
				pass
		# print(dct)
		n_dct = {n[:-1] for n in old.readlines()}
		for i in n_dct:
			if not i in dct:
				new.write(i + "\n")
		# print(n_dct)




# 846106824 неугодный id


def main():
	parse()
	cleanup()

if __name__ == '__main__':
	main()
