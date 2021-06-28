# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

# Format and print the current date and time to include
# only the day of the week, the hour, and the minute.
print(f"{current_date_and_time:%A %I:%M %p}")