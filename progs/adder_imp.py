ui = input("enter ',' seperated numbers:" )
ui = ui.split(',')  # list of strings
total = 0
for num in ui:
    total += int(num)
    
print("Summation: ", total)