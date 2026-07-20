dictionary = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

take = input("Enter a Roman numeral: ").upper()
result = 0

for i in range(len(take)):
    if i > 0 and dictionary[take[i]] > dictionary[take[i - 1]]:
        result += dictionary[take[i]] - 2 * dictionary[take[i - 1]]
    else:
        result += dictionary[take[i]]
print("The integer value is:", result)
