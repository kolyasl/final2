from datetime import datetime

def spl():                      #  функція ,що робить розділ введених значень діапазону  на 2 окремих числа
    while True:                 #  і присвоює їх двом змінним ,щоб в подальшому використати їх
                                #  як значення початкового і кінцевого елементів діапазону'''
        try:
            your_diapasone = input("Please,enter your numbers diapasone  through space: ")
            stnew = your_diapasone.split(' ')
            n = int(stnew[0])
            m = int(stnew[1])
        except ValueError as error:
            print("{0}{1} It is not correct.Please try again".format(error,your_diapasone))
        except IndexError as error:
            print("{0}{1} it is not correct.Please try again".format(error, your_diapasone))
        else:
            if n != m :
                return n, m
                break
            else:
                print("Try input different numbers")

def counts(n):                 # функція для підрахунку  елементів
    count = 0
    for i in n:
        count += 1
    return count

def firstmid(s,f):             # функція для розрахунку першого середнього значення .
    row = list(range(s,f+1))   # Приймає 2 аргументи s-початкова значення діапазону f-кінцеве
    m = s + counts(row)/2
    return m

def secondmid(s,f):
    row = list(range(s,f+1))   # функція для розрахунку наступних середніх значеннь.
    m = counts(row)/2          # Аргументи такі ж як і в функції firstmid
    return m

def bisec():                   # функція знаходження загаданого числа
    st,fin = spl()             # використавує метод половинного ділення
    middle = firstmid(st,fin)
    middle = int(middle)
    start_time = datetime.now()
    coun = 1
    while True:
        print("{0} is your number?".format(middle))
        answer = input("Please enter Yes if I guessed .If not,enter More or Less ")
        answer = answer.lower()
        if answer == "yes":
            print("***********************************")
            print("BINGO!!!Your number is {0}".format(middle))
            break
        elif answer == "more":
            st = int(middle)
            middle = int(secondmid(st,fin)) + middle
            coun += 1
        elif answer == "less":
            fin = int(middle)
            middle = middle - int(secondmid(st, fin))
            coun += 1
        else:
            print("I think,you make mistake when was chosing More or Less ")
    final_time = datetime.now()
    timetosloving = final_time - start_time

    print("Time to solving {0}".format(timetosloving))
    print("Count tries {0}".format(coun))
bisec()