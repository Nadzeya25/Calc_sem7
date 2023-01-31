from logg import logging


def get_num_R():
    while True:
        try:
            r = float(input("""введите рациональное число - 
в виде десятичной дроби через точку либо целое число: """))
                        
        except ValueError:
            print("некорректный ввод, попробуйте еще раз")
            logging.error("некорректный ввод")
            continue
        else:
            return r


def get_num_Compl():
    while True:
        try:
            a = float(input("""введите значение a для комплексного числа:
 - десятичная дробь с точкой или целое число
                            """))
            b = float(input("""введите значение a для комплексного числа:
 - десятичная дробь с точкой или целое число
                            """))                                     
            ab = complex(a, b)
            

        except ValueError:
            logging.error("некорректный ввод")
            print("некорректный ввод значений, попробуйте еще раз")
            continue
        else:
            print(ab)
            return ab
        

        