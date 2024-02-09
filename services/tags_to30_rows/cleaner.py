from collections import Counter

filtered = 'filtered 06-08.02.2024.txt'
result = 'RESULT_from_FILTERED.txt'

with open(filtered, 'r') as l, open(result, 'w+') as r:
	new_lst = [i.split(',') for i in [line.strip() for line in l]]
	res_lst = [k for i in new_lst for k in i]
	cnt = dict(Counter([k for i in new_lst for k in i]))

	sorted_cnt = sorted(cnt.items(), key=lambda item: item[1], reverse=True)
	[r.write(f'    {key}\n') for key, value in sorted_cnt if value >= 10]

	# потом пройтись по нему Counter
	# потом хэштеги, которых больше 10 записать в новый файл
	# потом разбить их по 30 и добавить отступы от края, чтоб Ире пальцем тыкать удобно было