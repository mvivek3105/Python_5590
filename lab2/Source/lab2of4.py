bookumkc = {"ISL":60, "Algorithms":20, "Python":80}

mini = int(input("Enter the minimum price"))
maxi = int(input("Enter the maximum price"))

a = True

for (key,value) in bookumkc.items():
    if mini <= value <= maxi:
     if a:
         print('Available books for the price range', mini, 'and', maxi,'are:')
         a = False
     print(key)
    else:
     exit(print('No books available'))