import re

key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print(pattern1.findall(key))

c = "diskcluster-cloud-16 sadfalkdfalsjl cloud-16 asdfjalsjdlfalj diskcluster-cloud-16-ssd"
pattern = re.compile(r'[^ ]*cloud-16[^ ]*')
print(pattern.findall(c))