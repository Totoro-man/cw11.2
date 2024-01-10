def uppercase_str(s):
    """blablabla"""
    return s.upper()


def uppercase_first(s):
    """blablabla"""
    sl = s.split()
    for i in sl:
        i.capitalize()
    return " ".join(sl)
