# Adding the Number of Hours Worked
dailyHours = [float(input(f"Enter hours worked on Day {i + 1}: ")) for i in range(5)]

# Finding the Most Hours Worked
mostHours = max(dailyHours)

# Finding the Total Hours Worked
totalHours = sum(dailyHours)