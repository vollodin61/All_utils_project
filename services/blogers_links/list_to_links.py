import re


with open("services/blogers_links/list.txt", "r", encoding="utf-8") as lst, open("services/blogers_links/link.txt", "a+", encoding="utf-8") as lnk:
	[lnk.write(re.sub(r"\d+. ", '', f"{i[:-25]}\n")) for i in set(lst.readlines()) if i.strip()]
