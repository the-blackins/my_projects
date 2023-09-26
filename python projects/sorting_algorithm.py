# creating an algorithm that sorts numbers in ascending order within the range of 25 numbers 
#  approach:
# stage 1: recieve input(int) from user to start the count increament and store it in a variable "start_index"
# stage 2:
#  creating a for loop that  increaments the value within the range of "start_index" and "end_index".
# stage 3:
#  the increament values of the index is then pushed or appended to an array.
# stage 4:
#  the stored array is then shuffled and then reasigned to its  variable  
# stage 5:
#  applying the given sorting algorithm,  the shuffled array is then sorted in an asending order
# stage 6:
#  test and run. 

import random 
 
start_index = int(input("What integer would you want the count to begin with: ")) #stage 1
# adds 26 numbers to the start_index so in the for loop its within the range of the 1st index to the 25th index
end_index = start_index + 26 

num_arr = []
for i in range(start_index,end_index): #stage 2
    num_arr.append(i) #stage 3
    random.shuffle(num_arr) #stage 4

print("shuffled array: ", num_arr)

# stage 5:
def selection_sort (arr):   
    n = len(arr)
    for i in range(n): 
        min_idk = i
        for j in range(i+1,  n):
            if arr[j] < arr[min_idk]:
                min_idk = j
        arr[i], arr[min_idk ] = arr[min_idk], arr[i]
    return arr 

# stage 6
sorted_numbers = selection_sort(num_arr)
print("sorted array:  ", sorted_numbers)



# insertion sorting:
# stage 5
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#stage 6
sorted_numbers = insertion_sort(num_arr)
print("sorted array:  ", sorted_numbers)


# exchange sort or bubble sort:

#stage 5
def exchange_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n -i -1):
            if arr[j] > arr[j + 1]:
                # swap elements
                arr[j] , arr[j + 1 ] =  arr[j + 1], arr[j];
    return arr

#stage 6
sorted_numbers = exchange_sort(num_arr)
print("sorted array:  ", sorted_numbers)
 
