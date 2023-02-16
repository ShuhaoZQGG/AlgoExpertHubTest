def caesarCipherEncryptor(string, key):
    # Write your code here.
    offset = ord("a")
    result = ""
    for char in string:
        ascii = ord(char)
        new_ascii = (ascii - offset + key) % 26 + offset
        result += chr(new_ascii)
    return result

