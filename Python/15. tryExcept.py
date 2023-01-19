##Lets define a function that divides a list of numbers into a factor of any factor we want to use
def divide_elements_of_list(list, divisor):
    try:
        return [i/divisor for i in list]
    except ZeroDivisionError as e:
        print(e)                                ##when there is an indeterminate division the algorithm does not break but proceeds to execute another script.
        return list

my_list = list(range(10))
divisor=2                                       ##Test the script with this value
divisor2 = 0                                    ##Test the script with 0 value

print(divide_elements_of_list(my_list, divisor2))
