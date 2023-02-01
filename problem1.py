def add(n): #function definition
    if n/10<=1: #base code
        return 1
    else:
        return n%10+add(int(n/10)) #call itself
      

print(add(54))
