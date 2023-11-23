from pyrogram import Client
from environs import Env

env = Env()
env.read_env()
id_ifill = env("id_ifill")
hash_ifill = env("hash_ifill")
my_id = env("my_id")
my_hash = env("my_hash")
my_tg_id = env("my_tg_id")
my_tg_username = env("my_tg_username")
ira_id = env("ira_id")
ira_hash = env("ira_hash")
file_to_who_send = 'data/lst_TOSEND_PRIGLOS.txt'
ids_set = set()
new_ids_list = list()


def attach():
	with Client('ira_acc', ira_id, ira_hash) as app:
		app.send_message(my_tg_username, text='Client successfully created')


attach()
