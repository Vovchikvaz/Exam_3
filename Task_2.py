# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково
# слева-направо и справа-налево. Иначе – False
def Func(a):
    a = ''.join(filter(lambda x: x.isalpha(),a.lower()))
    if a == a[::-1]:
        return 'True'
    else:
        return 'False'
a = input('Введите любое слово: ')
if Func(a):
 print('True')
else:
 print('False')




