def full_name (first, last):
    name = f'{first} {last}'
    return name;

# Take Parameters In Order
# name = full_name ("John", "Doe");

name = full_name (last="Doe", first= "John");
print (name);


# **args
def famousName (first, last, **addition):
    print(f'{first} {last}\n')
    print (addition['profession'])

    for key, value in addition.items():
    
        print (key,":",value)
    

famousName("John", "Dof", profession="S/W", city="New York", status="Active")

# def function_name (num1, num2, *args, **kargs)

def a_lot (num1, num2):
    add = num1 + num2
    mult = num1*num2
    dev = num1/num2

    return add, mult, dev;

everything= a_lot(5,3);
print(everything)