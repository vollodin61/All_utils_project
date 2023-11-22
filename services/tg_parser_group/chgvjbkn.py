import re

with (open('tmp_noname_list.txt', 'r', encoding='utf-8') as off,
	  open('clear_tmp_noname_list.txt', 'a+', encoding='utf-8') as onn,
	  open('bad_boys.txt', 'r', encoding='utf-8') as bbads):
	dct = dict()
	for k in bbads.readlines():
		username = re.findall(pattern=r"[A-Za-z]\S+", string=k)
		tel = re.match(pattern=r"/d+", string=k)
		try:
			print(username[0])
		except Exception as e:
			# print(k[:-1])
			pass
	# for i in {m for m in off.readlines()}:
	# 	if i not in bbads.readlines():
	# 		onn.write(i)


