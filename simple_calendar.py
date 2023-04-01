
import datetime  # import datetime
import calendar  # import calendar

# Get current date and time
current_data = datetime.datetime.now()
# Format current date and time
format_data = current_data.strftime("%Y-%m-%d | %H:%M")

# Print current date and time
print(f"Current year: {format_data}")
