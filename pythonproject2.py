from datetime import datetime

# Input: Date of birth from user
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert input to datetime object
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Get today's date
today = datetime.today()

# Calculate age
age = today.year - dob.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Output
print(f"You are {age} years old.")
