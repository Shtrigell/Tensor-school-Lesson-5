def summary(*args):
    z = 0
    for num in args:
        z += num
    return z
sum_list=[]
sum_list = input("Введите числа, через пробел, которые хотите сложить. Для выхода нахмите Enter. ").split()
for i in range (len(sum_list)):
    try:
        sum_list[i]=int(sum_list[i])
    except ValueError:
        print("Неверный формат данных, данные будут удалены.")
        sum_list[i]=0
a=summary(*sum_list)
print("Ваша сумма: ", a)