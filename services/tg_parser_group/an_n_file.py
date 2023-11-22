with open('tmp_list.txt', 'r', encoding='utf-8') as old, open('clear_tmp_list.txt', 'a+', encoding='utf-8') as new:
	for i in {i for i in old.readlines()}:
		new.write(i)

with open('tmp_noname_list.txt', 'r', encoding='utf-8') as off, open('clear_tmp_noname_list.txt', 'a+', encoding='utf-8') as onn:
	for i in {m for m in off.readlines()}:
		onn.write(i)


# TODO убрать из рассылки всех, кто уже проходил Кошку