# print(5, 6, 8)
# n = None
# print(type(n))
# n='gkjhk'
# print(n)
# print(type(n))

# print('Введите превое число')
# a=int(input())
# b=int(input("Введите второе число: "))
# print(a, '+',b, '=', a+b)

# a=round(1.567897, 3)
# print(a)

# iter=2
# iter+=3 # iter=iter+3
# iter-=4
# iter*=5
# iter/=5
# iter//=5
# iter%=5
# iter**=5

# a=1>4
# print(a)
# a=1<4 and 5>2
# print(a)
# a=1==2
# print(a)
# a=1!=2
# print(a)
# a='qwe'
# b='qwe'
# print(a==b)
# a=1<3<3<10
# print(a)

# username=input('Введите имя: ')
# if username=='Маша':
#     print('Ура, это Маша!')
# elif username =='Марина':
#     print('Я так ждала Вас, Марина!')
# elif username=='Ильнар':
#     print('Ильнар-топ')
# else:
#     print('Привет, ',username)

# n=423
# summa=0
# while  n>0:
#     x=n%10
#     summa=summa+x
#     n=n//10
#     print(summa)
# print(summa)

# i=0
# while i<5:
#     # if i==3:
#     #     break
#     i=i+1
# else:
#     print('Пожалуй')
#     print('хватит')
# print(i)

# n=int(input('Введите число: '))
# flag=True
# i=2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print('Минимальный делитель числа: ', i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in 1, -2, 3, 14, 5:
#     print(i)

# r=range(5)
# print(r)
# r=range(2, 5)
# print(r)
# r=range(0, -5)
# print(r)
# r=range(1, 10, 2)
# print(r)
# r=range(100, 0, -20)

# print(r)

# r=range(100, 0, -20)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

# a='qwerty'
# print(a[2])

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё','ЕЩЁ'))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
