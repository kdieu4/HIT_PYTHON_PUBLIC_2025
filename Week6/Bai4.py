def format_phone_number(phone_number):
    formatted_number = ""
    for char in phone_number:
        if char.isdigit():
            formatted_number = formatted_number + char
    if formatted_number[0] != "0" or len(formatted_number) != 10:
        return "Invalid phone number"
    return formatted_number


print(format_phone_number("09_645jhgkhj60712"))
