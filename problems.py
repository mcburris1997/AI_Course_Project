'''
This file will contain your the code for your problems. 
'''

# Problem
# Creating a digital solution that requires a combination of apps, automations, reports, datasets, documentation, and trainings.
# Each component takes a certain number of hours to complete. Datasets need to be done first, apps, automations, and reports need to be done second and can be done at the same time,
# documentation comes next, then trainings comes last.

# Define hour values required to complete each component
app = 16
automation = 8
report = 12
documention = 4
trainings = 4

# Define initial hour values available - 1 full-time developer specializing in dataset, app, automation, and documentation. 1 part-time developer specializing in reports and training.
full_time_dev = 80
part_time_dev = 40

# Situation 1 - A solution that requires 1 app, 1 automattions, 1 documentation, and 1 training

# Initial message to start collecting project requirement data
print("Thank you for submitting your project request. Please answer yes or no to the following questions to help plan your project.")

# Gather whether or not apps are needed for the project
var_app = input("Do you need an app? Please type Y for yes and N for No: ")
if var_app == "Y":
    var_app = 16
else:
     var_app = 0
     print("Sounds good")

# Gather whether or not multiple apps are needed for the project
var_app_multiple = int(input("Do you need more than one? If not, type 1 and if so, type how many. Ex. 2, 4, ... : "))
if var_app_multiple == 1:
     var_app_multiple = var_app
else:
     var_app_multiple = var_app_multiple






# Gather inputs

