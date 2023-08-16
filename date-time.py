from datetime import datetime
import pytz

# Get the current time in the 'Asia/Kolkata' timezone
timezone = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(timezone)

# Format the current time according to the desired format
formatted_time = current_time.strftime('%a %d %m:%H:%M:%S %Z %Y')

print(formatted_time)
