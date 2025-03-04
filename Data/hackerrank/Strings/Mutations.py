def mutate_string(string, position, character):
    aux_string = list(string)
    aux_string[position] = character
    aux_string = "".join(aux_string)
    return aux_string

