import re


def parse_reg_plate(reg_plate):
    if re.match('|'.join(['^[А-Я]{2}\\d{4}[А-Я]{2}$',
                          '\\d{2}\\s\\d{3}-\\d{2}[А-Я]{2}',
                          '[а-я]\\d{5}[А-Я]{2}']), reg_plate):
        return reg_plate
    else:
        return None


print(parse_reg_plate('АА1234КК'))
