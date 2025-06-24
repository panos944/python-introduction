# Constants
SECONDS_IN_A_MINUTE = 60;
SECONDS_IN_AN_HOUR = 3600;
SECONDS_IN_A_DAY = 86400;

# propmt
total_seconds = int(input("Enter the number of seconds: "))

# Calculations
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

seconds = seconds_remaining

print(f"{total_seconds} seconds is equal to");
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")