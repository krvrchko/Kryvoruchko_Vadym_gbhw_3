num_input = input('Введите, пожалуйста, число от 1 до 10 на английском прописью:')

def num_translate(num):
  num_dict = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'
  }
  if num in num_dict:
    return num_dict[num]
  else:
    return None

print(num_translate(num_input))