'''
This file will contain your the code for your problems. 
'''

# Problem
# Creating a digital solution that requires a combination of apps, automations, reports, datasets, documentation, and trainings.
# Each component takes a certain number of hours to complete. Datasets need to be done first, apps, automations, and reports need to be done second and can be done at the same time,
# documentation comes next, then trainings comes last.

# Define hour values required to complete each component
dataset = 4
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
print("Thank you for submitting your project request. Please answer the following questions using whole number integers (ex. 1, 2, 3...) to help plan your project.")

# Gather whether or not apps are needed for the project
var_app = 0
var_app = int(input("Do you need an app? If yes, please type how many (ex. 1, 2, 4...) and if not then type 0 for No: "))
if var_app == 0:
    var_app = 0
    print("Sounds good")
else:
     var_app = (var_app * 16)
     print(f"Your requested app component(s) will take {var_app} hours to complete.")

# Check to see if the requested components exceed current development hours
if var_app <= 80:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This request would take {var_app} hours but only {full_time_dev} hours are currently available.")

# Update the development hours that are available
full_time_dev = (full_time_dev - var_app)
print(f"Remaining development hours available: {full_time_dev}")

# Gather whether or not automations are needed for the project
var_automation = 0
var_automation = int(input("Do you need an automation? If yes, please type how many (ex. 1, 2, 4, ...) and if not then type 0 for No: "))
if var_automation == 0:
     print("Sounds good")
else:
     var_automation = (var_automation * 8)
     print(var_automation)
var_running_total = (var_app + var_automation)

# Check to see if the requested components exceed current development hours
if var_running_total <= 80:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. this project component would take {var_automation} hours to complete but only {full_time_dev} hours are available")






# Gather inputs

