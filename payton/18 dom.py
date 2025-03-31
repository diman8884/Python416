import re

email="123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"

regex = r'([\w0-9-._]+@[\w0-9-.]+[\w0-9]{2,3})'

print(re.findall(regex, email))

