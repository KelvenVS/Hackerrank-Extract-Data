import numpy


if __name__ == '__main__':
    input_lenght = input().split()
    
    arr_aux = []
    for _ in range(int(input_lenght[0])):
        arr_aux.append(input().split())
    
    my_array = numpy.array(arr_aux, dtype=int)
    
    print(numpy.mean(my_array , axis = 1))
    print(numpy.var(my_array , axis = 0))
    std_value = numpy.std(my_array)
    std_value = 0.0 if std_value == 0.0 else f'{std_value:.11f}'
    print(std_value)
