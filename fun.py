# Names: Arshia Sharifi, Nicholas Shebetun, Stewart Bustard,  Zil Pavdighada
# Please use the csv file accompanied with the zip file because this one 
# has some modification to the timestamps of the keys in the to make them
# easier to read and call in the for loops
import numpy as np
from matplotlib import pyplot as plt
import csv
#method for running the files
"""
The file reader below initially converts the csv to a dictionary using the time stamps 
then with the for loop, each time stamp is allocated to its own respect list.
The values inside each key of the dictionary are ordered chronologically there fore
the responses of the first person are the value inside index 1 of each key
"""
with open('ChatGPT.csv', encoding = 'utf-8-sig') as f:
    loop = csv.DictReader(f) #converts each row of the csv file into a dictionary
    genders = []
    age = []
    highest_education = []
    employment_status = []
    country = []
    knowledge = []
    ethical = []
    assignment = []
    learning = []
    dependency = []
    comments = []
    for x in loop:
        genders.append(x['gender'])
        age.append(x['age'])
        highest_education.append(x['university'])
        employment_status.append(x['job'])
        country.append(x['country'])
        knowledge.append(x['heard'])
        ethical.append(x['ethical'])
        assignment.append(x['assignment'])
        learning.append(x['learning'])
        dependency.append(x['agree'])
        comments.append(x['other'])

# the ones that don't have _ are the titles of the x-axis
# the ones that have _ in the label carry the values of the those specific values from the timestamps
# we used count method to count each instance of a response within the respect list that we updated in the csv reader
gender = ["Male", "Female"]
gender_stats = [genders.count('Male'), genders.count('Female')]

ages = ["15-22 years old", "23-30 years old"]
ages_stats = [age.count("15-22 years old"), age.count("23-30 years old")]

education = ['Undergraduate Student', 'Graduate Student', 'Other instructor']
education_stats = [highest_education.count('Undergraduate Student'), highest_education.count('Graduate Student'), highest_education.count('Other instructor (TA, study helper, etc.)')] 

jobs = ['Employed full-time', 'Employed Part-time', 'Student', 'Self-Employed']
jobs_stats = [employment_status.count('Employed full-time (40+ hours a week)'), employment_status.count('Employed part-time (less than 40 hours a week)'), employment_status.count('Student'), employment_status.count('Self-employed')]

countries = ['Canada', 'USA', 'Other']
countries_stats = [country.count('Canada'), country.count('USA'), country.count('Other')]

#Dependent graphs
heard = ["Yes", "No"]
heard_stats = [knowledge.count("Yes"), knowledge.count("No")]

ethics = ['Yes', 'Neutral', 'No']
ethics_stats = [ethical.count('Yes'), ethical.count('Neutral'), ethical.count('No')]

assignments = ["Yes", "No"]
assignment_stats = [assignment.count("Yes"), assignment.count("No")]

learnings = ["Yes", "Neutral", "No"]
learning_stats = [learning.count("Yes"), learning.count("Neutral"), learning.count("No")]

dependencies = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
dependency_stats = [dependency.count("Strongly agree"), dependency.count("Agree"), dependency.count("Neutral"), dependency.count("Disagree"), dependency.count("Strongly disagree")]

# Since the last question was multiple selection, we couldn't simply use count because some people types their own 
# Comments in the other were personalized and there was no pattern in those responses
"""
When splitting, sometimes the first character was a space so I checked for that and filtered the list
based on the options available on the survey and also based on other if those responses
didn't match any of the survey options
"""
empty  =[]
for y in comments:
    mid = y.split(',')
    for a in mid:
        if a[0] == " ":
            empty.append(a[1:])
        else:
            empty.append(a)
count = 0
for x in empty:
    if x == "Researching difficult questions" or x == "Debates and discussions" or x == "Programming assignments":
        count += 1
        continue
    else:
        empty[count] = 'Other'
        count += 1
comment = ["Researching difficult questions", "Debates and discussions", "Programming assignments", "Other"]
comment_stats = [empty.count("Researching difficult questions"), empty.count("Debates and discussions"), empty.count("Programming assignments"), empty.count("Other")]

#Dependent vs independent
#this takes advantage of the that the list is ordered chronologically

#Gender vs ethics
"""
the following loops are the method that we used to compare the independent data to the dependent ones
each value in the males_ethics for instance relates to either yes, neutral or no
since the lists are ordered chronologically, we looped through the genders list,
if that element at that index is men, then we checked the index in the list we wanted to compare to
and increased the count of the number corresponsing to that value
"""
males_ethics = [0, 0, 0]
females_ethics = [0, 0, 0]
count = 0
for x in genders:
    if x == "Male":
        if ethical[count] == "Yes":
            males_ethics[0] += 1
            count += 1
        elif ethical[count] == "No":
            males_ethics[2] += 1
            count += 1
        else:
            males_ethics[1] += 1
            count += 1
    elif x == "Female":
        if ethical[count] == "Yes":
            females_ethics[0] += 1
            count += 1
        elif ethical[count] == "No":
            females_ethics[2] += 1
            count += 1
        else:
            females_ethics[1] += 1
            count += 1
    else:
        count += 1

#Age vs ethics
# Same method as before
age1522_ethics = [0, 0, 0]
age2330_ethics = [0, 0, 0]
count = 0
for y in age:
    if y == "15-22 years old":
        if ethical[count] == "Yes":
            age1522_ethics[0] += 1
            count += 1
        elif ethical[count] == "No":
            age1522_ethics[2] += 1
            count += 1
        else:
            age1522_ethics[1] += 1
            count += 1
    elif y == "23-30 years old":
        if ethical[count] == "Yes":
            age2330_ethics[0] += 1
            count += 1
        elif ethical[count] == "No":
            age2330_ethics[2] += 1
            count += 1
        else:
            age2330_ethics[1] += 1
            count += 1
    else:
        count += 1

#Age vs dependency

age1522_dependency = [0, 0, 0, 0, 0]
age2330_dependency = [0, 0, 0, 0, 0]
count = 0
for y in age:
    if y == "15-22 years old":
        if dependency[count] == "Strongly agree":
            age1522_dependency[0] += 1
            count += 1
        elif dependency[count] == "Agree":
            age1522_dependency[1] += 1
            count += 1
        elif dependency[count] == "Neutral":
            age1522_dependency[2] += 1
            count += 1
        elif dependency[count] == "Disagree":
            age1522_dependency[3] += 1
            count += 1
        else:
            age1522_dependency[4] += 1
            count += 1
    elif y == "23-30 years old":
        if dependency[count] == "Strongly agree":
            age2330_dependency[0] += 1
            count += 1
        elif dependency[count] == "Agree":
            age2330_dependency[1] += 1
            count += 1
        elif dependency[count] == "Neutral":
            age2330_dependency[2] += 1
            count += 1
        elif dependency[count] == "Disagree":
            age2330_dependency[3] += 1
            count += 1
        else:
            age1522_dependency[4] += 1
            count += 1
    else:
        count += 1

# first graph (Pie graphs)
# this is how we built a grid of graphs
# the subplot(2, 2)  is a 2x2 array
# [0, 0] corresponds to row 1 column 1
colors = ['red', 'tab:blue']
fig, axis = plt.subplots(2, 2) 
axis[0, 0].pie(gender_stats, autopct = '%2.1f%%', colors = colors, textprops = {'fontsize': 14})
axis[0, 0].set_title('Genders of the Participants', bbox={'facecolor':'0.8', 'pad':5})
axis[0, 0].legend(gender, bbox_to_anchor = (1, 0.5))

#second graph
# explode is for popping out a certain portion
colors = ['tab:green', 'cyan']
explode = [0.2, 0]
axis[0, 1].set_title('Ages of the Participants', bbox={'facecolor':'0.8', 'pad':5})
axis[0, 1].pie(ages_stats, autopct = '%2.1f%%', explode = explode, startangle = 45, colors = colors, textprops = {'fontsize': 14})
axis[0, 1].legend(ages, bbox_to_anchor = (1, 0.5))

#third graph
explode = [0.2, 0, 0]
axis[1, 0].pie(education_stats, autopct = '%2.1f%%',explode = explode, colors = ['tab:brown', 'cyan', 'red'], textprops = {'fontsize': 14})
axis[1, 0].set_title('Educational Background', bbox={'facecolor':'0.8', 'pad':5})
axis[1, 0].legend(education, bbox_to_anchor = (1, 0.5))

#fourth graph
explode = [0, 0, 0.2, 0]

axis[1, 1].pie(jobs_stats, autopct = '%2.1f%%', explode = explode, colors = ['tab:blue', 'purple', 'tab:orange', 'green'], textprops = {'fontsize': 14})
axis[1, 1].set_title('Employment Status', bbox={'facecolor':'0.8', 'pad':5})
axis[1, 1].legend(jobs, bbox_to_anchor = (1, 0.5))

plt.rcParams['figure.figsize'] = [7.50, 3.50]
plt.rcParams['figure.autolayout'] = True
plt.show()

#separation
# same method used for the pie graphs
fig, axis = plt.subplots(2, 2)

axis[0, 0].bar(ethics, ethics_stats, color = ['tab:orange', 'cyan', 'red'])
axis[0, 0].set_title("Number of People Who Think ChatGPT is Ethical", bbox={'facecolor':'0.8', 'pad':5})

axis[0, 1].bar(learnings, learning_stats, color = ['tab:blue', 'red', 'green'], width = 0.6)
axis[0, 1].set_title("Number of People Who Think ChatGPT Enhances Creativity/Learning", bbox={'facecolor':'0.8', 'pad':5})

axis[1, 0].bar(dependencies, dependency_stats, color = ["red", "tab:orange", "green", "cyan", "tab:blue"])
axis[1, 0].set_title("Number of People Who Think ChatGPT Will Increase the Dependency of Students on Technology", bbox={"facecolor":'0.8', 'pad':5})

axis[1, 1].bar(comment, comment_stats, color = ["cyan", "tab:orange", "green", "purple"])
axis[1, 1].set_title("What should Students Use ChatGPT For?", bbox={"facecolor":"0.8", "pad":5})
#changing the fonts of the x-axis
axis[0, 0].tick_params(axis='x', labelsize=16)
axis[0, 1].tick_params(axis='x', labelsize=16)
axis[1, 0].tick_params(axis='x', labelsize=16)
axis[1, 1].tick_params(axis='x', labelsize=10)
# this is for adding labels to the y axis of each graph
for ax in axis.flat:
    ax.set(ylabel='Number of People')
plt.show()

#gender vs ethical
# these are double bar graphs used to compare male resonses to female responses
X_axis = np.arange(len(ethics))
plt.bar(X_axis - 0.2, males_ethics, 0.4, label = "Males", color = "cyan")
plt.bar(X_axis + 0.2, females_ethics, 0.4, label = "Females", color = "green")

plt.xticks(X_axis, ethics)
plt.ylabel("Number of People")
plt.title("ChatGPT is Ethical in Academia: A Gendered Analysis", bbox={'facecolor':'0.8', 'pad':5})
plt.tick_params(axis = 'x', labelsize = 16)
plt.legend()
plt.show()

#age and ethics
# the code below are similar to the method used above
X_axis = np.arange(len(ethics))
plt.bar(X_axis - 0.2, age1522_ethics, 0.4, label = "Aged 15-22", color = "tab:blue")
plt.bar(X_axis + 0.2, age2330_ethics, 0.4, label = "Aged 23-30", color = "red")

plt.xticks(X_axis, ethics)
plt.ylabel("Number of People")
plt.title("ChatGPT is Ethical in Academia: Age Analysis", bbox={'facecolor':'0.8', 'pad':5})
plt.tick_params(axis = 'x', labelsize = 16)
plt.legend()
plt.show()

#age and dependency
X_axis = np.arange(len(dependencies))
plt.bar(X_axis - 0.2, age1522_dependency, 0.4, label = "Aged 15-22", color = "purple")
plt.bar(X_axis + 0.2, age2330_dependency, 0.4, label = "Aged 23-30", color = "mediumturquoise")

plt.xticks(X_axis, dependencies)
plt.ylabel("Number of people")
plt.title("ChatGPT Increases Dependency and Reduces and Self-Sufficiency: Age Analysis", bbox={'facecolor':'0.8', 'pad':5})
plt.tick_params(axis = 'x', labelsize = 16)
plt.legend()
plt.show()


