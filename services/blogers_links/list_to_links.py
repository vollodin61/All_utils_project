import re

FROM = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/FROM.txt'
TO = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/TO.txt'

with (open(FROM, "r", encoding="utf-8") as lst,
	  open(TO, "w+", encoding="utf-8") as lnk):
	[lnk.write(re.sub(r"\d+. ", '', f"{i[:-25]}\n")) for i in set(lst.readlines()) if i.strip()]
