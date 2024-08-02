#date of test: 26th October 2013

#Write a program in Python that reads an integer, checks that the read value is an 
#integer, and if it is even, writes half of the read number and if it is odd, writes 
#twice the read number.

def reads_integer():
    v = eval(input('Write an integer\n>'))
    if isinstance(v,int):
        if v % 2 == 0:
            return v/2
        else:
            return v*2
    else:
        raise ValueError ('the number is not an integer')


#Write a Python program that asks the user to provide
#integers (no need to check if the given number is an integer).
#When the user provides the number 0, your program writes a real that
#corresponds to the average of the numbers read.

def ask_integer():
    v = eval(input('Write an integer \n(0 to finish)\n>'))
    lista = []
    soma = 0
    
    while v != 0:
        lista = lista + [v]
        soma = soma + v
        v = eval(input('Write an integer\n> (0 to finish)'))
    
    if len(lista) == 0:
        print('No numbers typed')
    else:
        print(soma/len(lista))
    return

#Write a function in Python with the name numero_algarismos_impares
#which takes a positive integer, n, and returns the number of odd digits of n

def numero_algarismos_impares(num):
    sum_odd = 0
    if isinstance(num) and num>0:
        while num!=0:
            rest = num % 10
            if rest % 2 !=0:
                sum_odd = sum_odd + 1
            num = num // 10
    return sum_odd

#Write a function called part that takes as arguments a list,
#lst, and one element, e, and which returns a list of two elements, containing in
#first position the list with lst elements smaller than e, and in the second
#position the list with the elements of lst greater than or equal to e. It is not necessary
#Validate the arguments of your function.

def part(lst, e):
    s = []
    b = []
    for el in lst:
        if el < e:
            s = s + [el]
    else:
        b = b + [el]
    return [s, b]
