#  a function that takes a list and target parameter
# multiple variables :  start, middle/ end, steps
# recursion or while loop
# increase the steps each time a plits is done 
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start =  0
    end = len(list)
    steps = 0
    
    while(start<= end):
        print("steps", steps, ":" , str[list[start:end+1]])
        steps = steps + 1
        middle =  ( start + end ) // 2
            if element == list[middle]:
                return middle

print(5*2.9)