count = 0
def nome(count):
    print("Sabrina")
    count += 1
    if count == 10:
        return False
    else:
        nome(count)
        
    return(True)

nome(count)


def crashar(cont):
    print("oi", cont)
    if cont < 10:
        crashar(cont + 1)
    return(True)

crashar(0)