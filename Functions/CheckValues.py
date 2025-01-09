invalid = "Invalid number."
low = "Too low number."
high = "Too high number."

def CheckType(typ):  #"int", "float", "str"
    answer = input()
    while(True):
        answer = answer.replace(",", ".")
        try:
            float(answer)
            if(typ == "int"):
                return int(answer)
            elif(typ == "float"):
                return float(answer)
            else:
                print("Answer must be str. Try again!")
                answer = input()
        except ValueError:
            if(typ == "int"):
                print("Answer must be an integer. Try again!")
                answer = input()
            elif(typ == "float"):
                print("Answer must be a number. Try again!")
                answer = input()
            else:
                return answer

def CheckValues(typ, low, high, message_low, message_high):
    answer = CheckType(typ)
    if(high == -1):  #-1 means there's no limit
        while(answer < low):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(typ)
    else:
        while(answer < low or answer > high):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(typ)
            elif(answer > high):
                print(message_high, "Try again!")
                answer = CheckType(typ)
    return answer
