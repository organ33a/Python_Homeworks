
# ввести температуру (измеряется термометром) в цельсиях и программа конвертирует в фаренгейты
temp_MIN = 32
temp_MAX = 43

temp_Health_MIN = 35
temp_Health_MAX = 37

def convert_temp_f(temp_c):
    return round(temp_c * 1.8 + 32, 2)


def extra_message_print(temp_f):
    if (temp_c > temp_MAX) or (temp_c < temp_MIN):
        extra_message = f"Abnormal temperature {temp_f}. Check your thermometr!"
    else:
        if (temp_c >= temp_Health_MIN) and (temp_c <= temp_Health_MAX):
            extra_message = f"temperature {temp_f} is normal"
        elif (temp_c < temp_Health_MIN):
            extra_message = f"temp {temp_f} is lower than healthy"
        elif (temp_c > temp_Health_MAX):
            extra_message = f"temp {temp_f} is higher than healthy"

    return extra_message


temp_c = float(input("Input temperature in C:"))

print(f"Temp in F:{convert_temp_f(temp_c)}")

print(extra_message_print(convert_temp_f(temp_c)))