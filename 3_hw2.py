2.
a=10
b=160
if a > b:
  print("a")
else:
  print('b')

3.
if a + 135 == b or b + 135 == a:
  print('yes')
else:
  print('No')

4. 
def what_season(mounth_of_year):
  if mounth_of_year == 1 or mounth_of_year == 2 or mounth_of_year == 12:
    print('зима')
  elif mounth_of_year in range(3, 6):
    print('весна')
  elif 6 <= mounth_of_year <= 8:
    print('лето')
  else:
    print("осень")

what_season(7)

5.
a = 8
b = 15
c = 20
if a > 10 and b > 10 and c > 10:
  print("yes")
else:
  print("no")

6.
a = 8
b = -3
c = 6
d = -9
e = 4

def count_numbers(a, b, c, d, e):
  if a > 0 and b > 0 and c > 0 and d > 0 and e > 0:
    print() #хотела решить задачу, но не понимаю, какой функцией получить количество. Объясните, пожалуйста, решение.

7.
int_year = 5
int_month  = 12
def count(days = int_year * int_month * 29):
  print(days) #здесь тоже до конца не понимаю, как правильно записать
