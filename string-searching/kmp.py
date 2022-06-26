def find_kmp(string, text):
    str_len = len(string)
    if str_len == 0:
        return []
    txt_len = len(text)
    if txt_len == 0:
        return []
    if str_len > txt_len:
        return []
    res = []
    p = [0]*str_len
    j = 0
    for i in range(1, str_len):
        while j > 0 and string[j] != string[i]:
            j = p[j]
        if string[j] == string[i]:
            j += 1
        p[i] = j

    j = 0
    for i in range(txt_len):
        while j > 0 and string[j] != text[i]:
            j = p[j-1]
        if string[j] == text[i]:
            j += 1
        if j == str_len:
            res.append(i - str_len + 1)
            j = p[j-1]
    return res
