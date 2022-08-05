stop = True
items = {}
grocery_history = []
grand_total = 0


while stop == True:
    #set a list that helps you to add a new item to the list
    items.setdefault("name", []).append(input('Item name:\n'))
    items.setdefault("quantity", []).append(int(input('Quantity Purchased:\n')))
    items.setdefault("cost",[]).append(float(input('price per item:\n')))

    print('would you like to enter another item?')
    choice = str(input("Type 'c' for continue or 'q' to quit:\n"))

    if choice == 'c':
        stop = True
    else:
        stop = False
#this loop helps to iterate sufficiently for given item names
        for i in range(len(items['name'])):

            items_total = (items['quantity'][i]*items['cost'][i])
            grand_total += items_total
            print(items['name'][i],"@","$",items['cost'][i], "ea", "$", (items_total))

            #this part creates a history items for each sale for the given items names
            ith_history = [str(i+1)+'.Sale:' +str(items['quantity'][i]) + ' ' +items['name'][i] + 'from' + str(items['cost'][i])+ 'Total: ' +str(items_total)]
            grocery_history.append(ith_history)

print("Grand total: $", grand_total)
items_total=0