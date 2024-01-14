from pyrogram import Client
from environs import Env
# TODO тут криво работал вытаск из виртуального окружения id & hash
env = Env()
env.read_env()
id_ifill = env("id_ifill")
hash_ifill = env("hash_ifill")
my_id = env("my_id")
my_hash = env("my_hash")
my_admin_id = env("my_admin_id")
my_admin_hash = env("my_admin_hash")
# print(id_ifill, hash_ifill, my_id, my_hash)

chat_lst = [-1002018146453,
	# -756776870,
	# -1001527541226,
	# -1001981041874,
	# -687677378,
	# -900547806,
	#
	# -1001684131407,  # какой-то забагованный чат, почему-то с ним не срабатывает (руками пользователей достал из него)
]

cli = Client(name='_parser_', api_id=my_admin_id, api_hash=my_admin_hash)
cli.start()
for _ in chat_lst:
	lst = cli.get_chat_members(_)
	for i in lst:
		with open("_list_users.txt", "a+", encoding="utf-8") as f:
			if i.user.username:
				f.write(f"{i.user.username}\n")
			else:
				f.write(f"{i.user.id}\n")
				with open("ids_temp_lst.txt", "a+", encoding="utf-8") as nf:
					nf.write(f"{i.user.id} {i.user.first_name} {i.user.last_name}\n")
cli.stop()
