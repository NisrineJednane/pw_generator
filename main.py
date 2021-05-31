print("strong password generator")
user_letters = int(input("how many letters in your password?\n"))
user_numbers = int(input("how many numbers in your password?\n"))
user_symbols = int(input("how many symbols in your password?\n"))

selected_letters = random.sample(letters, user_letters)
selected_numbers = random.sample(numbers, user_numbers)
selected_symbols = random.sample(symbols, user_symbols)
pw_list = [selected_letters, selected_numbers, selected_symbols]
# flatten the list to scramble the results and join them into one string:
pw_list = [item for items in pw_list for item in items]
pw_result = pw_list[:]
random.shuffle(pw_result)
pw = ""
for x in pw_result:
    pw += x
print(pw)
