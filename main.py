import re
import csv
from pprint import pprint
from collections import defaultdict

# читаем адресную книгу в формате CSV в список contacts_list

with open("/Users/anastasiaklimanova/Desktop/phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

new_list = []
for i, l in enumerate(contacts_list):
  l = (" ".join(l[:2]).split())
  contacts_list[i][0] = l[0]
  contacts_list[i][1] = l[1]
  try:
    contacts_list[i][2] = l[2]
  except IndexError:
    pass

data = defaultdict(list)
for info in contacts_list:
  key = tuple(info[:2])
  for item in info:
    if item not in data[key]:
      data[key].append(item)

new_list = list(data.values())
# pprint(new_list)
text = ''
for i, l in enumerate(contacts_list):
  text += contacts_list[i][5] + ' '
# # pprint(text)

pattern = re.compile(r'(7|\+7|8)\s*\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2})(\s*\(?(доб.)\s*(\d{4})\)?)?')
s_pattern = r'+7(\2)\3-\4-\5;\7\8'
result = pattern.sub(s_pattern, text)
# pprint(result)
a = result.split()
# pprint(a)

for el, s in zip(new_list, a):
  el[5] = s

pprint(new_list)


# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_list)

