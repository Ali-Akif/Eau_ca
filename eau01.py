zero = 0

for i in range(zero, 100):
    for i in range(1,100):
        print(f"{"0" if zero < 10 else ""}{zero} {"0" if i < 10 else ""}{i}", end=", ")

    zero +=1
    
        

    