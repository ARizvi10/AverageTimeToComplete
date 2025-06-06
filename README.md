Overview

Task Time Tracker is a simple yet effective program that helps users estimate how long a task will take based on their personal work habits. I created this program because I often felt that I would estimate in my head that a task would take a certain amount of days based off my preconcieved idea of how long I spend per day, but that estimate was clouded by bias and incorrect assumptions. By tracking the amount of time spent on a task each day, the program calculates the average daily time investment and projects the number of days required to complete similar tasks in the future accurately.

Features

-Input daily time spent on a task

-Tracks how many days have passed

-Calculate average time spent per day

-Estimate how many days a task will take to complete based on this average

How It Works

The user inputs the time (in hours, minutes, etc.) they spend on a task each day.
The program keeps track of how many days have passed since tracking began.
It calculates the average time spent on the task per day.
When given a total estimated task time, the program can estimate how many more days are needed to complete the task based on the user's past average.

Example Use Case

Imagine you're writing a research paper. You log how long you spend writing each day:

Day 1: 2 hours

Day 2: 1.5 hours

Day 3: 2.5 hours

The program calculates your average as 2 hours per day. If you estimate the paper will take 10 hours total, the program predicts it will take you approximately 5 days to finish.

Features to still be implemented:

Currently, the program overwrites the txt file where the data is stored every time it is ran, this is due to my usage of "w" mode of opening files instead of in-place file editing. 
I still need to update the code to reflect this change, so as of now, I consider this program non-functional.
