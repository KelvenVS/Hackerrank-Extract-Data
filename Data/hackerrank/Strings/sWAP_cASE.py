def swap_case(s):
    aux_list = []
    for i in s.strip():
        if i.isupper():
            aux_list.append(i.lower())
        else:
            aux_list.append(i.upper())
    return "".join(aux_list)

