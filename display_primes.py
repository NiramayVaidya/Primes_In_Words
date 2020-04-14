def main():
    word = "AND"
    hun = "HUNDRED"
    thou = "THOUSAND"
    num = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    num1 = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
    tens = ["TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start > end:
        print("Invalid range")
    elif start < 2:
        print("Invalid range")
    elif end > 9999:
        print("Invalid range")
    else:    
        for i in range(start, end + 1):
            for j in range(2, i):
                if (i % j) == 0:
                    break
            if i == 2:
                j = 2
            if j == i - 1 or i == 2:
                i1 = str(i)
                length = len(i1)
                if length == 1:
                    print(num[int(i1[0]) - 1])
                elif length == 2 and int(i1) < 20:
                    print(num1[int(i1[1])])
                elif length == 2:
                    if int(i1[1]) != 0:
                        print(tens[int(i1[0]) - 2], num[int(i1[1]) - 1])
                    else:
                        print(tens[int(i1[0]) - 2])
                elif length == 3:
                    if int(i1[1]) == 0 and int(i1[2]) == 0:
                        print(num[int(i1[0]) - 1], hun)
                    elif int(i1[2]) == 0:
                        if int(i1[1]) == 1:
                            print(num[int(i1[0]) - 1], hun, word, num1[0]);
                        else:
                            print(num[int(i1[0]) - 1], hun, word, tens[int(i1[1]) - 2])
                    elif int(i1[1]) == 0:
                        print(num[int(i1[0]) - 1], hun, word, num[int(i1[2]) - 1])
                    elif int(i1[1]) == 1 and int(i1[2]) != 0:
                        print(num[int(i1[0]) - 1], hun, word, num1[int(i1[2])])
                    elif int(i1[1]) != 1 and int(i1[2]) != 0:
                        print(num[int(i1[0]) - 1], hun, word, tens[int(i1[1]) - 2], num[int(i1[2]) - 1])
                elif length == 4:
                    if int(i1[1]) == 0 and int(i1[2]) == 0 and int(i1[3]) == 0:
                        print(num[int(i1[0]) - 1], thou)
                    elif int(i1[1]) == 0 and int(i1[2]) == 0 and int(i1[3]) != 0:
                        print(num[int(i1[0]) - 1], thou, word, num[int(i1[3]) - 1])
                    elif int(i1[1]) == 0 and int(i1[2]) != 0 and int(i1[3]) == 0:
                        if int(i1[2]) == 1:
                            print(num[int(i1[0]) - 1], thou, word, num1[0])
                        else:
                            print(num[int(i1[0]) - 1], thou, word, tens[int(i1[2]) - 2])
                    elif int(i1[1]) != 0 and int(i1[2]) == 0 and int(i1[3]) == 0:
                        print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun)
                    elif int(i1[1]) != 0 and int(i1[2]) != 0 and int(i1[3]) == 0:
                        if int(i1[2]) == 1:
                            print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun, word, num1[0])
                        else:
                            print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun, word, tens[int(i1[2]) - 2])
                    elif int(i1[1]) == 0 and int(i1[2]) != 0 and int(i1[3]) != 0:
                        if int(i1[2]) == 1:
                            print(num[int(i1[0]) - 1], thou, word, num1[int(i1[3])])
                        else:
                            print(num[int(i1[0]) - 1], thou, word, tens[int(i1[2]) - 2], num[int(i1[3]) - 1])
                    elif int(i1[1]) != 0 and int(i1[2]) == 0 and int(i1[3]) != 0:
                        print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun, word, num[int(i1[3]) - 1])
                    elif int(i1[1]) != 0 and int(i1[2]) != 0 and int(i1[3]) != 0:
                        if int(i1[2] == 1):
                            print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun, word, num1[int(i1[3])])
                        else:
                            print(num[int(i1[0]) - 1], thou, num[int(i1[1]) - 1], hun, word, tens[int(i1[2]) - 2], num[int(i1[3]) - 1])
            elif j < i - 1:
                continue
            
if __name__ == '__main__':
        main()
        