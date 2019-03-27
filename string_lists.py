def is_polindrom(_str):
    _str = _str.lower().replace(" ", "")
    d = 1
    for ii in list(range(int(len(_str) / 2))):
        if _str[ii] == _str[ii - d]:
            d += 2
            continue
        return False
    return True


str_to_check = input("Your string: ")
print(is_polindrom(str_to_check))
