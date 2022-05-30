#Write a function that accepts any number of integers as positional arguments and any number
 #of a student's attributes as keyword arguments and prints the result of multiplying all of 
 #the integers with a customized greeting based on the keyword arguments. Name the function 
 #multiply_and_greet.
 
def greet_and_multiply(*args, **kwargs):
    keys = kwargs.keys()
    multiplication = 1
    for num in args:
        multiplication = num
        return multiplication
    if "age" in keys:
        return f"Hi {kwargs['name']} from {kwargs['age']}"
    elif "country" in keys:
        return f"Hi {kwargs['name']} from {kwargs['country']}"
    elif "name" in keys:
        return f"Hi {kwargs['name']}"
    else:
        return f"Hi Hoppers"
        