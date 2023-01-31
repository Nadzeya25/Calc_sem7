from excep import zero_err
from logg import logging
logging.info('start program')
# from excep import check_true_int
# from excep import check_zero
from math_op import*

# на 1.38 минуте сем7
def menu():
    
    while True:
        type_num = input("""выберите , с каким типом чисел работать:
          1 - Рациональные
          2 - Комплексные
          """)
        match type_num:
            case '1':
                menu_calc_R()
            case '2':
                menu_calc_C()               

            case _:
                logging.warning("неверный ввод пункта меню")
                print("введите еще раз")
                menu()

from view import get_num_Compl, get_num_R
def menu_calc_C():# меню для комплексных
    num1 = get_num_Compl()
    num2 = get_num_Compl()
    type_op_C = input("""выберите тип операции с комплексными числами:
      1 - сумма
      2 - разность
      3 - произведение
      4 - обычное деление
      5 - выбрать другие комплексные числа
      6 - переход к меню выбора типов чисел
      """ )

    while True:

        match type_op_C:

            case "1":
                print(sum(num1, num2))
                menu()
            case "2":
                print(sub((num1, num2)))
                menu()
            case "3":
                print(mult(num1, num2))
                menu()
            case "4":
                if num2 == 0:
                    print(zero_err())
                    menu_calc_C()
                else:
                    print(div_all(num1, num2))
                    menu()
            case '5':
                logging.info("Stop program")
                menu_calc_C()        
            case '6':
                logging.info("Stop program")
                menu()
                
            case _:
                logging.error("неверный ввод пункта меню")
                print('введите еще раз')
                break 


def menu_calc_R():# меню для рациональных
    num1 = get_num_R()
    num2 = get_num_R()    
    
    type_op_R = input("""выберите тип операции с рациональными числами:
      1 - сумма
      2 - разность
      3 - произведение
      4 - обычное деление
      5 - целочисленное деление
      6 - остаток от деления
      7 - степень числа
      8 - выбрать другие рациональные числа
      9 - переход к меню выбора типов чисел
      """ )

    while True:

        match type_op_R:
            case "1":
                print(sum(num1, num2))
                menu()
            case "2":
                print(sub(num1, num2))
                menu()
            case "3":
                print(mult(num1, num2))
                menu()
            case "4":
                if num2 == 0:
                    print(zero_err())
                    menu_calc_R()
                else:
                    print(round(div_all(num1, num2)), 2)
                    menu()
            case "5":
                if num2 == 0:
                    print(zero_err())
                    menu_calc_R()
                else:
                    print(div_int(num1, num2))
                    menu()
            case "6":
                if num2 == 0:
                    print(zero_err())
                    menu_calc_R()
                else:
                    print(div_rem(num1, num2))
                    menu()
            case "7":
                print(pow(num1, int(num2)))
                menu_calc_R()
            case '8':
                logging.info("Stop program")
                menu_calc_R()                
            case '9':
                logging.info("Stop program")
                menu()                                      
            case _:
                logging.error("неверный ввод пункта меню")
                print('введите еще раз')
                break
           
      


