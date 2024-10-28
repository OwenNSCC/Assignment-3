# Adding the Number of Hours Worked
dailyHours = [float(input(f"Enter hours worked on Day {i + 1}: ")) for i in range(5)]

# Finding the Most Hours Worked
mostHours = max(dailyHours)

# Finding the Total Hours Worked
totalHours = sum(dailyHours)

# Finding Average Hours Worked
averageHours = totalHours / 5

# Finding Day with Most Hours
mostHourDays = [i + 1 for i in range(5) if dailyHours[i] == mostHours]

# Days Slacked off 
slackedDays = [i + 1 for i in range(5) if dailyHours[i] < 7]

# Printing Outputs
print("-------------------------------------------------------------------------")
print(f"The most hours worked was on Day #{mostHourDays} when you worked {mostHours}")