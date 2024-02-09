import re

FROM = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/FROM.txt'
TO = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/TO.txt'
RESULT = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/RESULT.txt'

with (open(FROM, "r", encoding="utf-8") as lst, open(TO, "w+", encoding="utf-8") as lnk):
	[lnk.write(re.match(pattern=r".+(?=\?)", string=i).group(0) + "\n") for i in set(lst.readlines()) if i.strip()]

with (open(TO, 'r') as edit, open(RESULT, 'w', encoding='utf-8') as result):
	count = 0
	for line in edit:
		if count < 4:
			result.write(line)
			count += 1
		else:
			count = 0
			result.write('\n')
