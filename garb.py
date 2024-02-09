import re


st = "https://www.instagram.com/vika.sheshura?igsh=aGc3MHo1dW8wZTlj"
# # st = "?jfggjhfg"
# print(re.findall(pattern=r"(?<!\?).+", string=st))

t = "alex Sergey Ivanov?, Ivan Ivanov"
print(re.findall(pattern=r".+(?=\?)", string=st))
