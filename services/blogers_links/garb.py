import re

tx = 'sadl;fkj?123;kj'

d = re.findall(r".+\?", tx)

print(d[0][:-1])
