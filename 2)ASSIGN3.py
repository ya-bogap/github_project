import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Q 2)A The files are downloaded from kaggle

# Q2)B
#Opening both files as panda dataframes
myfile1 = pd.read_csv("/Users/yaswanthbogapurapu/Desktop/tit_train.csv")
myfile1.head()
myfile2 = pd.read_csv("/Users/yaswanthbogapurapu/Desktop/tit_test.csv")
myfile2.head()

#CONCAT THE TWO DATA FILES
concat_file = pd.concat([myfile1,myfile2])
print(concat_file)


#Q 2)C
#GIVE SUMMARY OF THE DATA FILES
print(concat_file.describe())


#Q 2)D
#PLOTTING A HISTOGRAM OF AGE OF PEOPLE IN TITANIC
plt.hist(concat_file['Age'],color = 'red')
plt.xlabel('Age')
plt.ylabel('Rate')
plt.title('Age distribution of passengers')
plt.show()

#PLOTTING A HISTOGRAM SEGGREGATED BY SURVIVALSHIP OF PASSENGERS BIASED BY AGE
plt.hist(concat_file[concat_file['Survived']== 0]['Age'],color = 'blue',label = 'not survived people ')
plt.hist(concat_file[concat_file['Survived']==1]['Age'],color = 'red',label ='survived people')
plt.xlabel('Age')
plt.ylabel('Rate')
plt.title('age of people seggregated by survivalship')
plt.legend()
plt.show()



# Q 2)E
#percentage of people survived on titanic
survived = concat_file['Survived'].value_counts(normalize=True) * 100
survived.plot(kind='bar', color=['red', 'blue'])
plt.title('Overall Survival Percentage')
plt.xlabel('Survived')
plt.ylabel('Percentage')
plt.show()


#suvival percentage seggregated by sex
survival_by_sex = concat_file.groupby('Sex')['Survived'].mean()* 100
survival_by_sex.plot(kind ='bar',color=['red', 'green'])
plt.title('Survival Percentage by Sex')
plt.xlabel('Sex')
plt.ylabel('Percentage')
plt.show()

#Q 2)F
#Box plot showing passenger class vs survived
sns.boxplot(x ='Pclass',y ='Survived',data = concat_file)
plt.xlabel('class of passenger')
plt.ylabel('Age')
plt.title('Survived passengers and their class')
plt.show()

#survived vs passenger class seggregated by sex
sns.boxplot(x='Pclass',y='Survived',hue = 'Sex',data = concat_file)
plt.xlabel('class of passenger')
plt.ylabel('age of passenger')
plt.title('Passenger age distribution by sex and class,Survived passengers')
plt.legend(title = 'passenger sex',loc ='upper right')
plt.show()


#Q 2)G
   
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

























