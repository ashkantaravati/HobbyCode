def encrypt(original,shift,increasing=True):
    if increasing==False:
        shift=-shift
    encrypted=str()
    for char in list(original):
        encrypted=encrypted+str(chr(ord(char)+int(shift)))
    return encrypted
#__main__
print(encrypt(input(),input()))
 
    


