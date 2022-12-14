def check_passwd(passwd):
    if len(passwd)>=6:
       if [s for s in passwd if s in '1234567890']:
           if passwd.isdigit()==False:
               if ("password" in passwd.lower())!=True:
                   return True
               else:
                   return False
           else:
               return False
       else:
           return False
    else:
        return False
result=check_passwd(input("Введите ваш пароль: "))# Проверка данного ввода выполняется в функции, блок try..except не требуется.
if result==True:
    print("Ваш пароль прошёл проверку !")
else:
    print("Ваш пароль не прошёл проверку !")

