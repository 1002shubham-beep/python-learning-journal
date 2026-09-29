# Match-case statement (switch): An alternative to using many 'elif' statements. Execute some code if a value matches a 'case'. Benefits: cleaner and syntax is more readable

# Instead of:
# def day_of_week(day):
#     if day == 1:
#         print("It's Monday")
#     elif day == 2:
#         print("It's Tuesday")
#     elif day == 3:
#         print("It's Wednesday")
#     elif day == 4:
#         print("It's Thursday")
#     elif day == 5:
#         print("It's Friday")
#     elif day == 6:
#         print("It's Saturday")
#     elif day == 7:
#         print("It's Sunday")
#     else:
#         print("Not a valid day")

# day_of_week(1)

# We do this:
# def day_of_week(day):
#     match day:
#         case 1:
#             print("It's Monday")
#         case 2:
#             print("It's Tuesday")
#         case 3:
#             print("It's Wednesday")
#         case 4:
#             print("It's Thursday")
#         case 5:
#             print("It's Friday")
#         case 6:
#             print("It's Saturday")
#         case 7:
#             print("It's Sunday")
#         case _:
#             print("Not a valid day")

# day_of_week(5)

#Checking weekend

def weekend_checker(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return "Not a valid day"

print(weekend_checker("pizza"))