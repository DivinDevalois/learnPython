def steps(number):
    compteur=0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")  
    while number!=1:
        compteur=compteur+1
        if number%2!=0:
            number=3*number+1
            
        else:
            number=number//2
    return  compteur 
    pass
