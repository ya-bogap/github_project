
#QUESTION-1 A
import numpy as np

x = int(input('Enter the number:'))

def generate_fibonacci_numbers(X):
    if X <= 0:
        return np.array([])  # Return an empty array for X <= 0
    elif X == 1:
        return np.array([0])  # Special case for X = 1
    
    fib_numbers = np.ones(X, dtype=np.int64)
    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(2, X):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers

# Now, you can use this function to create a NumPy array with the first X Fibonacci numbers:
fibonacci_array = generate_fibonacci_numbers(x)

# Printing the result
print(fibonacci_array)


#QUESTION 1 B
import numpy as np



def fib_list(x):
    fib_list_ = []
    first_number = 0
    second_number = 1
    fib_list_.append(0)
    fib_list_.append(1)
    for i in range(x): 
        c = first_number + second_number
        fib_list_.append(c)
        first_number = second_number
        second_number = c
    return fib_list_ 
 
num = 20
generated_sequence = fib_list(num)
final_array = np.array(generated_sequence)  

print(generated_sequence) 



#QUESTION-1 C
import numpy as np
import matplotlib.pyplot as plt

def fib_list(x):
    fib_list_ = []
    first_number = 0
    second_number = 1
    fib_list_.append(0)
    fib_list_.append(1)
    for i in range(x): 
        c = first_number + second_number
        fib_list_.append(c)
        first_number = second_number
        second_number = c
    return fib_list_ 
 
num = 20
generated_sequence = fib_list(num)
final_array = np.array(generated_sequence)  

print(generated_sequence) 

#  Question 1)C
#Open an empty list
quotient = []
quotient.append(1)
quotient.append(1)
#The next subsequent number in the list should be the quotient of the previous numbers
for i in range(2,num):
    result_value = generated_sequence[i]/generated_sequence[i-1]
    quotient.append(result_value)
print(quotient)

array_quotient = np.array(quotient)

print(array_quotient)



difference =[]
difference.append(0)
difference.append(0)
#Create a loop where the subsequent number is difference of the previous number in the fibonacci list
for i in range(3,num):
    result_value = quotient[i]-quotient[i-1]
    difference.append(result_value)
print(difference)
array_difference = np.array(difference)
print(array_difference)


#QUESTION-1) D
plt.plot(final_array, label = 'fib_list')
plt.plot(array_quotient,label = 'Quotient')
plt.plot(array_difference,label = 'Difference')
plt.xlabel('x')
plt.ylabel('y')
plt.title('GRAPH')
plt.legend()
plt.show()


#Question-1(E
#These values appear to be converging at 18.9 on x-axis and -2e+01 on y-axis























