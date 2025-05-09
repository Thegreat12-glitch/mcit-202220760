# Prompt the user to enter the number of days
days = int(input("Enter the number of days: "))
 
# Convert days to seconds
seconds = days * 86400  # 1 day = 86400 seconds
 
# Convert seconds to minutes
minutes = seconds // 60  # Integer division to get full minutes
 
# Display the results
print(f"{days} day(s) is equal to {seconds} second(s) or {minutes} minute(s).")