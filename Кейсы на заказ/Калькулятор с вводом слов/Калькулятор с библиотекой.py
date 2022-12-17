from numerizer import numerize
import translators as ts
import translators.server as tss

calc = input("Введите действие: ")

def calc_one(calc):
    if "разделить" in calc:

        calc = calc.split("разделить")
        first_num = numerize(ts.translate_text(calc[0]))
        sec_num = numerize(ts.translate_text(calc[-1]))
        conclusion = int(first_num) // int(sec_num)
        print(int(first_num) // int(sec_num))


    elif "умножить" in calc:

        calc = calc.split("умножить")
        first_num = numerize(ts.translate_text(calc[0]))
        sec_num = numerize(ts.translate_text(calc[-1]))
        print(int(first_num) * int(sec_num))

    elif "минус" in calc:

        calc = calc.split("минус")
        first_num = numerize(ts.translate_text(calc[0]))
        sec_num = numerize(ts.translate_text(calc[-1]))
        print(int(first_num) - int(sec_num))

    elif "плюс" in calc:

        calc = calc.split("плюс")
        first_num = numerize(ts.translate_text(calc[0]))
        sec_num = numerize(ts.translate_text(calc[-1]))
        print(int(first_num) + int(sec_num))

calc_one(calc)