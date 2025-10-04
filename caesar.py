def caesar_encrypt(text, shift):
    """
    این الگوریتم سزار است
    Args:
        text (str): متن اصلی
        shift (int): مثدار جابجایی 1-25
    
    Returns:
        str: متن رمزشده 
    """
    result = ""
    for char in text:
        if char.isupper():
           position = ord(char) - ord('A')
           new_position = (position + shift) % 26
           new_char = chr(new_position + ord('A'))
           result += new_char
        elif char.islower():
           position = ord(char) - ord('a')
           new_position = (position + shift) % 26
           new_char = chr(new_position + ord('a'))
           result += new_char
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


secret = "khoor"
decrypted = []
for i in range(26):
     decrypted.append(caesar_decrypt(secret, i)+"\n")

with open('secret.txt', 'w') as f:
    f.writelines(decrypted)


