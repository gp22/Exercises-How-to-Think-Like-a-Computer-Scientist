# Write a function called rot13 that uses the Caesar cipher to encrypt a
# message. The Caesar cipher works like a substitution cipher but each
# character is replaced by the character 13 characters to ‘its right’ in
# the alphabet. So for example the letter a becomes the letter n. If a
# letter is past the middle of the alphabet then the counting wraps
# around to the letter a again, so n becomes a, o becomes b and so on.
# Hint: Whenever you talk about things wrapping around its a good idea
# to think of modulo arithmetic.

def rot13(mess):
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_mess = ''

    for char in mess:
        # if char is not a letter, leave it alone
        if char not in alpha_lower and char not in alpha_upper:
            encrypted_mess += char
            continue
        
        # if char is a letter, apply the cipher
        if char in alpha_lower:
            rotated_index = alpha_lower.index(char) + 13
            if rotated_index < 26:
                encrypted_mess += alpha_lower[rotated_index]
            else:    
                encrypted_mess += alpha_lower[rotated_index % 26]
            
        else: # char in alpha_upper:
            rotated_index = alpha_upper.index(char) + 13
            if rotated_index < 26:
                encrypted_mess += alpha_upper[rotated_index]
            else:    
                encrypted_mess += alpha_upper[rotated_index % 26]

    return encrypted_mess
        
print(rot13('Encrypt this string.'))
