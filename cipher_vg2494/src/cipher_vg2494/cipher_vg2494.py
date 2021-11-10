def cipher(text, shift, encrypt=True):
    """
    The function below is a cipher function
    That uses a simple character shift cipher to encrypt words.
    
    Inputs
    ------
    text = a string value that need to be encrypted or decrypted
    shift = an int value designating of letters to shift each character in the text. Can be a positive or negative value. 
    encrypt = if "True", the function will conduct a positive shift on the text. if "False", a negative shift.
              The "False", functionality is meant to help decrypt text back to its original readable format.
    
    Output
    ------
    A transformation of original text value, encrypted or decrypted
    
    Examples
    --------
    Encrypting: 
    cipher ("hello", 2, encrypt = True)
    >>> returns: "ignnq"
    
    Decrypting:
    cipher ("ignnq", 2, encrypt = False)
    >>> returns: "hello"
    """  
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text