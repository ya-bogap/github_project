#Q 1)A
import numpy library from python using import numpy as np 
Give an input function to ask the user for input in integers.
define a function in such a way which appends the list of numbers to the numoy array for fibonacci numbers using if and elif, and use for loop to print the required number of elements. Print the array of numbers.

#Q 1)B
Import numpy library from python using using import numpy as np.
Define a fibonacci list which limits the output to 20 elements only.
Append the generated list (generated_sequence)of numbers to a numpy array(final_array)
Check the result using the print function.

Q 1) C
Create a list fib_list which limits the fibonacci numbers to 20 elements.
Append the first(0) and second(1) values in a fibonacci number to the fib_list.
Now create a for loop which adds the previous two numbers to a result. 
Open a list 2 in which the subsequent number is the quotient of the previous two numbers and append the result_value to the list2.Here the first number is 1.
The generated list of numbers are put into an array called array_quotient.
And again open a list 3 and append zero to the list. The range for list 3 starts from third fibonacci number and ends with the input number.The  subsequent number in this is the result_value  of the difference between the previous two numbers.
The resulted list of numbers are put into an array called array_difference.

Q 1)D
Plot all the resulted list of numbers in each and every case by importing matplotlib.pyplot as plt.
Give plt.plot(array,label) to plot graph and give the label to x-axis ,y-axis and title to the graph and use plt.show() to show the result

Q 1)E
#These values appear to be converging at 18.9 on x-axis and -2e+01 on y-axis.









Q 2)A
The data training and the testing data are downloaded from the kaggle after signing up.

Q 2)B
Import the panda using import pandas as pd and then the .csv(ttraining and testing data) files are read using pd.read_csv(path of the file). And display the first few rows using file.head(). And we can specify the number of lines to be displayed by putiing the number in .head().

Concatenate both the (training data and testing data) files into a single file using the pd.concat([file1 ,file2]).

Q 2)C
The summary of the files is created using the print(concatenatedfile.describe())

Q 2)D
 A histogram showing the distribution of age of people on the Titanic is created by importing the matplotlib.pyplot as plt.
 Use plt.hist(filename['Age'],color of graph)
     name the x-axis
     name the y-axis
     give title
     display the graph.
 
A histogram showing the distribution of age of people on the Titanic segregated by survivalship is created from the above concatenated data.
The matplot library is imported into python and the survived and dead passengers in the titanic are seperated by giving the function and respective color to each graph and the x-axis and y-axis are labelled , graph is titled and then displayed.


Q 2)E
Create a  dataset
Calculate the overall survival percentage by taking the sum of 'Survived' values and dividing it by the total number of passengers.
And then the data is grouped by 'Sex' and calculate the survival percentages for each group.
Create two bar charts, one for the overall survival percentage and another for survival percentages segregated by sex and label the x and y axes and give title to the graph and display it.


Q 2)F
import seaborn
Plot the boxplot by using sns.boxplot and giving all the necessary parameters.
label the x and y axes and give the legend(title , location,label) and disply the graph.

Import seaborn and use sns.boxplot and give the x- axis and y-axis parametre and data.
Label the x and y axes and give a title to the wholr boxplot.
Give the description of legend and also its location.
and display the graph.


Q 2)G
#Age Distribution:
#The age distribution was right-skewed, with a notable presence of young and elderly passengers.
#Survival Percentage:
#A significant number of passengers did not survive the disaster, with fewer survivors.
#Survival by Sex:
#More females survived compared to males, reflecting the "women and children first" policy.
#Survival by Passenger Class:
#First-class passengers had better survival chances compared to second and third-class passengers.
#Survival by Passenger Class Segregated by Sex:
#Survival rates were generally higher for first-class passengers, both for males and females.
#These concise conclusions capture the key findings from the Titanic dataset analysis.
