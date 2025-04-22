from datetime import datetime, timedelta
import os
print("Hello, This program takes the amount of time you spent doing a task, gives you the average based off all "
      "previous times, and lets you estimate how long a new task will take.")
filename = "times.txt"

#creates the file if it does not already exist
if not os.path.isfile(filename):
    with open(filename, "w") as f:
        f.write("")

#Finds the last time the program ran in the times.txt file, which is needed to see if a day has passed.
#Stores the datetime of the last time ran into the lastRun variable.
with open("times.txt", "r") as f:
    for line in f:
        if line.startswith("Last time ran: "):
            parts = line.strip().split(": ")
            if len(parts) == 3:
                lastRun = datetime(parts[0], parts[1], parts[2])
now = datetime.now()

with open("times.txt", "w") as f1:
    f1.write("Last time ran: " + now.isoformat())

#Need this for program to be able to run the first time
try:
    lastRun
except NameError:
    lastRun = now

#Checks if there is a day or more of difference between the last time ran and now, if there is then it goes
#to the "Days: " section of the text file and adds 1 to signify a day passing.
if now - lastRun >= timedelta(days=1):
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("Days: "):
                parts = line.strip().split(": ", 1)
                if len(parts) == 2:
                    days = parts[1]
    with open("times.txt", "w") as file:
        NewDays = int(days) + 1
        file.write("Days: " + str(NewDays))

userInput = input("To get started: \n"
      "Press 1 to input a time \n"
      "Press 2 to get an estimate \n"
      "Input: ")


#Takes the user input of the hours they wish to enter for the day, and adds it to the total hours from the previous days
#Rewrites the file after "Time: " to have the updated number. This feature is completed and functional.
if userInput == "1":
    userInputTime = input("enter the time in hours: ")
    data = 0
    with open("times.txt", "r") as file:
        for line in file:
            if line.startswith("Time: "):
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    data = parts[1] #extracts the data from after "Time: " I can use this to update it, or get the
                    #estimates, but to do that I need the days also
    with open("times.txt", "w") as file:
        time = int(data) + int(userInputTime)
        file.write("Time: " + str(time))

#So far, this just extracts the number after "Time: " which is the total number of hours spent on a task ever,
#Need to update this with 3 features
#       1. Check how many days have passed
#       2. Calculate an average by dividing the total time by total number of days
#       3. Calculate an estimate by dividing the estimated time of the task the average time per day and then printing it
if userInput == "2":
    userInputEstimate = input("enter the estimated time of the task: ")
    with open("times.txt", "r") as file:
        for line in file:
            if line.startswith("Time: "):
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    data = parts[1] #extracts the data from after "Time: " I can use this to update it, or get the
                    #estimates, but to do that I need the days also
                print(line)

            #UNTESTED CODE SO FAR, EVERYTHING ABOVE WORKS
            if line.startswith("Days: "):
                part = line.strip().split(": ")
                if len(part) == 2:
                    days = part[1] #Should extract the data after "Days: " This is still untested
    average = data/int(days)
    estimate = float(userInputEstimate)/average
    print("The task will take you: " + str(estimate) + "Days at your current rate of " + str(average) + "hours per day.")



