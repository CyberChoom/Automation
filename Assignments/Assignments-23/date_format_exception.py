from datetime import datetime

provided_date = input("Enter any date in the specified format (YYYY-MM-DD): ")
try:
    date_format = datetime.strptime(provided_date, "%Y-%m-%d")
    # Or date_format = date.fromisoformat(provided_date)
    weekday = datetime.strftime(date_format, "%A")
    print(f"It's {weekday}!")
except ValueError:
    print("The date you provided is in the wrong format, please try again.")
