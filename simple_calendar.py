
import datetime  # import datetime
import calendar  # import calendar

# Get current date and time
current_data = datetime.datetime.now()
# Format current date and time
format_data = current_data.strftime("%Y-%m-%d | %H:%M")

# Print current date and time
print(f"Current year: {format_data}")

# ANSI escape codes for coloring input prompts
RED = "\033[31m"
RESET = "\033[0m"

# Input year with validation
year_name = int(input(f"{RED}Enter year: {RESET}"))
while year_name < 1900 or year_name > 2100:
    print("Incorrect, please try again!")
    year_name = int(input(f"{RED}Enter year: {RESET}"))


# Input month with validation
month_name = int(input(f"{RED}Enter month (1-12): {RESET}"))
while month_name < 1 or month_name > 12:
    print("Incorrect, please try again!")
    month_name = int(input(f"{RED}Enter month (1-12): {RESET}"))

# Input day with validation
day_name = int(input(f"{RED}Enter day (1-31): {RESET}"))
while day_name < 1 or day_name > 31:
    print("Incorrect, please try again!")
    day_name = int(input(f"{RED}Enter day (1-31): {RESET}"))
