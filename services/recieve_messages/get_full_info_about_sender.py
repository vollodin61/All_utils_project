import logging
from datetime import datetime

from pyrogram import Client
from pyrogram.types import Message
from environs import Env
# TODO эта хуйня не работает!!!!!!!!
"-1253838063 - Лингвистика общий чат"
env = Env()
env.read_env()
ira_id = env('ira_id')
ira_hash = env('ira_hash')
# TODO эта хуйня не работает!!!!!!!!

client = Client('getter', api_id=ira_id, api_hash=ira_hash)

# TODO эта хуйня не работает!!!!!!!!
@client.on_message()
async def full_info_from_all_msgs(cli: Client, msg: Message):
	logging.basicConfig(level=logging.DEBUG)
	if msg.from_user.id == -211148784:
		print(env('ira_tg_id'))
		try:
			with open('data/full_info_from_all_msgs.txt', 'a+', encoding='utf-8') as info, \
				open('data/errors.txt', 'a+', encoding='utf-8') as errors:
				info.write(msg.forward_from_chat())
				# info.write(cli.get_chat())
		except Exception as err:
			errors.write(str(err))

# TODO эта хуйня не работает!!!!!!!!


try:
	print('Ира-бот запускаетсо')
	client.run()
	print('Ира-бот остановлен')
except Exception as err:
	err_text = f'\n{datetime.now()} - Не запустился бот - {err}'
	with open("log.txt", "a+", encoding="utf-8") as l:
		l.write(err_text)
