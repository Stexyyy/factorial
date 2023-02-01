def sum(n): #function definition
    if n<=1: #base code
        return 1
    else:
        return n+sum(n-1) #call itself
      

print(sum(5))
