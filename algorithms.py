'''
This file will contain implementations of each algorithm/agent type.
'''

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

# Define initial hour values available - 1 full-time developer specializing in dataset, app, automation, and documentation.
# 1 part-time developer specializing in reports and training.
full_time_dev = 80
part_time_dev = 40

# This code can be used to run various project scenarios. It is designed to determine if a project can be taken on
# given the fact that there is 1 full-time and 1 part-time developer both specializing is different key areas.

# Initial message to start collecting project requirement data
print("Thank you for submitting your project request. Please answer the following questions using whole number integers (ex. 1, 2, 3...) to help plan your project.")

# Gather whether or not new datasets are needed for this project
var_datasets = 0
var_datasets = int(input("Do you need a new dataset? If yes, please type how many (ex. 1, 2, 4, ...) and if not then type 0 for No: "))
if var_datasets == 0:
     var_datasets = 0
     print("Sounds good")
else:
     var_datasets = (var_datasets * 4)
     print(f"Your requested dataset component(s) will take {var_datasets} hours to complete")

# Store total number of datasets for final output
datasets_output = (var_datasets/4)

# Check to see if the requested components exceed available development hours
if var_datasets <= 80:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This request would take {var_datasets} hours but only {full_time_dev} hours are currently available.")

# Update the development hours that are available
full_time_dev = (full_time_dev - var_datasets)
print(f"Remaining development hours available: {full_time_dev}")

# Gather whether or not apps are needed for the project
var_app = 0
var_app = int(input("Do you need an app? If yes, please type how many (ex. 1, 2, 4...) and if not then type 0 for No: "))
if var_app == 0:
    var_app = 0
    print("Sounds good")
else:
     var_app = (var_app * 16)
     print(f"Your requested app component(s) will take {var_app} hours to complete.")
var_running_total = (var_datasets + var_app)

# Store total number of apps for final output
apps_output = (var_app/16)

# Check to see if the requested components exceed available development hours
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
var_running_total = (var_datasets + var_app + var_automation)

# Store total number of automations for final output
automations_output = (var_automation/8)

# Check to see if the requested components exceed available development hours
if var_running_total <= 80:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This project component would take {var_automation} hours to complete but only {full_time_dev} hours are available")

# Update the development hours that are available
full_time_dev = (full_time_dev - var_automation)
print(f"Remaining development hours available: {full_time_dev}")

# Gather whether or not reports are needed for the project
var_reports = 0
var_reports = int(input("Do you need a report? If yes, please type how many (ex. 1, 2, 4, ...) and if not then type 0 for No: "))
if var_reports == 0:
     print("Sounds good")
else:
     var_reports = (var_reports * 12)
     print(var_reports)
var_running_total_2 = (var_reports)

# Store total number of reports for final output
reports_output = (var_reports/12)

# Check to see if the requested components exceed available development hours
if var_running_total_2 <= 40:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This project component would take {var_reports} hours to complete but only {part_time_dev} hours are available")

# Update the development hours that are available
part_time_dev = (part_time_dev - var_reports)
print(f"Remaining development hours available: {part_time_dev}")

# Gather whether or not documentation is needed for the project
var_documentation = 0
var_documentation = int(input("Do you need documentation? If yes, please type 1 and if no, please type 0: "))
if var_documentation == 0:
     print("Sounds good")
else:
     var_documentation = 4
     print(var_documentation)
var_running_total = (var_datasets + var_app + var_automation + var_documentation)

# Store whether or not documentation is needed
if var_documentation == 0:
     documentation_output = 0
else:
     documentation_output = 1

# Check to see if the requested components exceed available development hours
if var_running_total <= 80:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This project component would take {var_documentation} hours to complete but only {full_time_dev} hours are available")

# Update the development hours that are available
full_time_dev = (full_time_dev - var_documentation)
print(f"Remaining development hours available: {full_time_dev}")

# Gather whether or not training is needed for the project
var_training = 0
var_training = int(input("Do you need training? If yes, please type 1 and if no, please type 0: "))
if var_training == 0:
     print("Sounds good")
else:
     var_training = 4
     print(var_training)
var_running_total_2 = (var_reports + var_training)

# Store whether or not training is needed
if var_training == 0:
     training_output = 0
else:
     training_output = 1

# Check to see if the requested components exceed the available development hours
if var_running_total_2 <= 40:
     print("Development time is available to meet this request!")
else:
     print(f"Sorry, development time is NOT available to meet this request. This project component would take {var_training} hours to complete but only {part_time_dev} hours are available")

# Update the development hours that are available
part_time_dev = (part_time_dev - var_training)
print(f"Remaining development hours available: {part_time_dev}")

# Print final output
print(f"Awesome, so for your project you need {datasets_output} new datasets, {apps_output} apps, {automations_output} automations, {reports_output} reports, {documentation_output} documentation, and {training_output} training. The team will work diligently to fulfill your request, and keep you updated! Thank you.")
                         
# Source
# https://docs.python.org/3/tutorial/controlflow.html
