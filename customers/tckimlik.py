def isValidTCID(value):
    value = str(value)
    
    if int(value[0]) == 0:
        return False
    
    digits = [int(d) for d in str(value)]
    
   
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    
   
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    
    
    return True