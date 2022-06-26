def find_n(string, text):
    str_len = len(string)
    if str_len == 0:
        return []
    txt_len = len(text)
    if txt_len == 0:
        return []
    if str_len > txt_len:
        return []
    res = []
    for i in range(txt_len - len(string) + 1):
        if text[i] == string[0]:
            j = 0
            while j < len(string):
                if text[i+j] != string[j]:
                    break
                j += 1
                if len(string) == j:
                    res.append(i)
    return res
