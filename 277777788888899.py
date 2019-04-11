counter = 0
number = input("Number:")
while True:
    result = 1
    digits = [int(i) for i in str(number)]
    if len(number) == 1:
        print("Total step:", end="")
        print(counter)
        break

    for j in digits:
        result *= j
    print(result)
    number = str(result)
    counter += 1
