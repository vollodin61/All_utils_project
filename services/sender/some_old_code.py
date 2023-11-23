
# def looper():
# 	logging.basicConfig(level=logging.INFO)
# 	total = 0  # всего ids считает скольким уже сделана попытка отправить
# 	temp_count = 0  # временная считалка, чтоб не спамить сильно
# 	loop_count = 0  # считает какой цикл отправки сейчас идёт
# 	total_loops = len(ids_set) / 11  # сколько всего циклов
# 	loops_remain = total_loops - loop_count  # сколько циклов осталось
# 	while total < len(ids_set):  # пока total меньше числа id в изначальном ids_set будет отправлять
# 		if temp_count < 10:
# 			if "10:00:00" < datetime.now().time().strftime("%H:%M:%S") < "21:00:00":
# 				temp_count += 1
# 				print("temp_count =", temp_count)
# 				total += 1
# 				print("total =", total)
# 				sender(lst_for_send)  # список кому отправить в этот цикл
# 				sleep(randint(3, 5))
# 		else:
# 			temp_count = 0
# 			print('temp_count =', temp_count)
# 			loop_count += 1
# 			print('loop_count =', loop_count)
# 			send_for_who(my_tg_id, loops_remain)
# 			sleep(randint(2521, 5442))
#

