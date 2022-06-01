def thesaurus(*args):
  dict_names = dict()
  for i in args:
    dict_names.setdefault(i[0], [])
    dict_names[i[0]].append(i)
  return dict_names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))