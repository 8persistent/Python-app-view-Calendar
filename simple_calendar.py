
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


# Custom function to print calendar with highlighted date


def print_calendar_with_highlight(year, month, day):
    cal = calendar.monthcalendar(year, month)
    print(calendar.month_name[month], year)
    print("Mo | Tu | We| Th| Fr| Sa| Su|")

    for week in cal:
        for i, date in enumerate(week):
            if date == day:
                print(f"[{date:2}]", end=" ")
            elif date == 0:
                print("   ", end=" ")
            else:
                print(f" {date:2}", end=" ")
        print()


# Use the custom function to print the calendar with the highlighted date
print_calendar_with_highlight(year_name, month_name, day_name)

# Display the selected date
print(
    f"{RED}Your selected date:{RESET} {day_name} {calendar.month_name[month_name]} {year_name}")
