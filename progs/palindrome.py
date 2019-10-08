ui = input("Enter you string: ").strip().lower().replace(' ','')
if ui == ui[::-1]:
    print("Its a palindrome!")
else:
    print("Its NOT a palindrome")
