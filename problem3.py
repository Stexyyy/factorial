def power(b, e): #function definition
    if e<=1: #base code
        return 1
    else:
        e -= 1
        return b+power(b, e-1) #call itself
      

print(power(5, 2))
