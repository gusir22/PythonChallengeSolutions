"""
Solved 12/11/22 by Gustavo Rivero

http://www.pythonchallenge.com/pc/def/map.html

"""
def reveal(message):
    """Decodes a secret message by iterating twice forward on each char of the secret str"""

    revelation = ""  # prepares empty revelation str
    ignore = " .()'!@#$%^&*-=+1234567890" # string of chars to ignore translating

    # iterate through message str
    for char in message:
        if char not in ignore:
            # this if clause loops letters around that would push past the z's 122 unicode to a's 97
            loop_limit = ord(char) > 120
            if loop_limit:
                # cycle around alphabet to a
                char = chr(ord(char)-24)
            else:
                # move forward twice as usual
                char = chr(ord(char)+2)

        revelation += char  # record new char into revelation message

    return revelation

if __name__ == "__main__":

    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    answer = "map"

    print("secret: ", reveal(message))
    print("answer: ", reveal(answer))
