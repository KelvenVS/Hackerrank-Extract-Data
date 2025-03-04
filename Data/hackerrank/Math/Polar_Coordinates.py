from cmath import phase
import re

def complex_numbers(tpl_values):
    real, img = tpl_values
    abs_part = abs(complex(float(real),float(img)))
    phase_part = phase(complex(float(real),float(img)))
    
    return f'{abs_part:.3f}\n{phase_part:.3f}'

if __name__ == '__main__':
    re_comp = re.compile(r'(-?\d+)([-+]\d+j)')
    value = re_comp.findall(input())
    real , img = value[0]
    
    print(complex_numbers((real,img.replace('j',''))))
    
