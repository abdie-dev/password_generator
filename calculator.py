print('Basic CLI math using python')

def fmath(operator):
    res = 0
    
    num_1 = int(input('Masukan angka pertama: '))
    num_2 = int(input('Masukan angka kedua: '))
    
    if operator == '-':
        res = num_1 - num_2
    elif operator == '+':
        res = num_1 + num_2
    
    print(res)

if __name__ == "__main__":
    operator_input = input('Masukan operator ("-", "+"): ').strip()
    fmath(operator=operator_input)