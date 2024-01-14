import re

FROM_List = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/FROM_List.txt'
TO_Set = '/home/i/MyPros/F/All_utils/All_utils_project/services/blogers_links/TO_Set.txt'

with (open(FROM_List, "r", encoding="utf-8") as lst, open(TO_Set, "w+", encoding="utf-8") as lnk):
	[lnk.write(i) for i in set(lst.readlines())]
