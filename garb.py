from datetime import datetime

print(datetime.now().time().strftime("%H:%M:%S") < "21:00:00")

