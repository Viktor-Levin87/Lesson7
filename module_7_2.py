def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    ans = {}
    s = 1
    for i in strings:
        k = file.tell()
        file.write(i + ' \n')
        ans.update({(s, k): i})
        s += 1
    file.close()
    return ans


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
