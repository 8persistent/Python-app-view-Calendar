
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
