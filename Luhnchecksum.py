def main():
    number = input("Number:")
    result = check(number)
    if result:
        print("vaild")
    else:
        print("notVaild")


def check(number):
    sum = 0
    result = 0
    digits = [int(i) for i in str(number)]
    for j in range(len(digits)):
        if (j % 2 != 0 and (len(digits) % 2 != 0)) or (j % 2 == 0 and (len(digits) % 2 == 0)):
            sum = digits[j] * 2
            if (len(str(sum)) != 1):
                for i in str(sum):
                    result += int(i)
            else:
                result += int(sum)
        else:
            result += int(digits[j])
    if (result % 10 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
