def find_rk(string, text):
    str_len = len(string)
    if str_len == 0:
        return []
    txt_len = len(text)
    if txt_len == 0:
        return []
    if str_len > txt_len:
        return []
    d = 512
    q = 294781
    res = []
    h = (d ** (str_len - 1)) % q

    p = 0
    t = 0

    for i in range(str_len):
        p = (d * p + ord(string[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(txt_len - str_len + 1):
        if p == t and text[i:i+str_len] == string:
            res.append(i)
        if i < txt_len - str_len:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+str_len])) % q
    return res
