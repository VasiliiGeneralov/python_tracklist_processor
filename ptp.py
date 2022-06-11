#!/usr/bin/env python3

def colon_to_sec(inp: str) -> int:
    inp = inp.lstrip().rstrip()
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
