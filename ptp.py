#!/usr/bin/env python3

def colon_to_sec(inp: str) -> int:
    inp_tokens = [token for token in inp.split(':') if token]
    result = 0
    for amount in inp_tokens:
        result = int(amount) + 60 * result
    return result


def sec_to_colon(inp: int) -> str:
    """
    Какой алгоритм?
      1. делим на 60
      2. остаток - количество секунд
      3. частное делим еще на 60
      4. остаток - количество минут
      5. частное делим еще на 60
      6. остаток - количество часов
      7. разделитель - ':'

    Поддержка большего количества итераций не имеет смысла с точки зрения
    формата, потому что нет такой единицы измерения как "60 часов", "60 * 60
    часов" и т.д., и уж тем более плохо представляется парсинг треклиста такой
    длительности, но с точки зрения алгоритма этот случай хочется поддержать
    """
    if not inp:
        return '0'
    d, m = divmod(inp, 60)
    return '{}:{}'.format(sec_to_colon(d), m)


if __name__ == '__main__':
    test = ''
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = ':1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '0:0:1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '0:0:0:1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = ':1:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '0:1:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:0:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '2:0:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '3:0:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '0:0:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:0:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:1:0'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:1:1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '1:2:3'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '3:2:1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
    test = '6:5:4:3:2:1'
    print(test, colon_to_sec(test), sec_to_colon(colon_to_sec(test)))
