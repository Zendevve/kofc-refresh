import re

f = r'd:\COMPROG\kofc\base\capstone_project\templates\event_form.html'

with open(f, 'r', encoding='utf-8') as file:
    content = file.read()

# Fix category comparisons
content = re.sub(r"category=='([^']+)'", r"category == '\1'", content)
content = re.sub(r'category=="([^"]+)"', r'category == "\1"', content)

# Fix council.id comparisons
content = re.sub(r'council\.id==council\.id', r'council.id == council.id', content)

with open(f, 'w', encoding='utf-8') as file:
    file.write(content)

print('Fixed!')
