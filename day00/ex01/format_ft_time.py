import time  # Importing the time module to work with time-related functions

# Get the current time in seconds since the Epoch (January 1, 1970)
seconds = time.time()

# Format the seconds in scientific notation with two decimal places
scientificNotation = format(seconds, '.2e')

# Format the seconds with comma separation and four decimal places
formatted_seconds = f"{seconds:,.4f}"

# Get the current date formatted as "Month Day Year" (e.g., "Oct 21 2022")
current_date = time.strftime("%b %d %Y")

# Print the seconds with both formats: comma-separated and scientific notation
print(f"Seconds since January 1, 1970: {formatted_seconds} or, {scientificNotation} in scientific notation")

# Print the current date in the specified format
print(current_date)
