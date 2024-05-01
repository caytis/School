from PIL import Image

"""This program hides text in an image using steganography. An image is provided by the user, and the user is prompted to enter a message to hide in the image. The program then hides the message in the image by altering the least significant bit of the green and blue values of the image's pixels. The user can then retrieve the hidden message from the image by running the program again and providing the image. The program will then extract the hidden message from the image and display it to the user."""

def hide_message(image, message):
    """Hides text in an image"""
    img = Image.open(image).convert("RGB")
    key = makeKey(img)
    pix = img.load()
    width, height = img.size
    space = int(width * height / 8)
    messageBin = "".join([bin(ord(i))[2:].zfill(8) for i in message])
    # encode messageBin with key
    encoded = []
    for i in range(len(messageBin)):
        encoded.append(str(int(messageBin[i]) ^ int(key[i % len(key)])))
    encoded = "".join(encoded)
    messageLength = len(encoded)
    messLenBin = bin(messageLength)[2:].zfill(16)
    toHide = messLenBin + encoded
    
    # check if the message can fit in the image
    if len(toHide) > space:
        raise ValueError("Message is too long to fit in the image")
    
    # hide the message in the image, alternating between g and b values in least significant bit, g in one pixel, b in the next
    for i in range(0, len(toHide) - 1, 2):
        x = i // 2 % width
        y = i // 2 % width
        r, g, b = pix[x, y]
        pix[x, y] = (r, g & 0b11111110 | int(toHide[i]), b)
        r, g, b = pix[x + 1, y + 1]
        img.putpixel((x + 1, y + 1), (r, g, b & 0b11111110 | int(toHide[i + 1])))
    
    img.save("hidden.png")
    return img


def show_message(image):
    """Shows the hidden message in an image"""
    img = Image.open(image).convert("RGB")
    key = makeKey(img)
    pix = img.load()
    width, height = img.size
    lengthBin = ""
    # alternating g and b values in least significant bit, g in one pixel, b in the next
    for i in range(0, 16, 2):
        x = i // 2 % width
        y = i // 2 % width
        r, firstg, b = pix[x, y]
        r, g, secondb = pix[x + 1, y + 1]
        lengthBin += str(firstg & 1)
        lengthBin += str(secondb & 1)
    # decode the length of the message
    messageLength = int(lengthBin, 2)
    messageBin = ""
    for i in range(16, messageLength * 8 + 16, 2):
        x = i // 2 % width
        y = i // 2 % width
        r, firstg, b = pix[x, y]
        r, g, secondb = pix[x + 1, y + 1]
        messageBin += str(firstg & 1)
        messageBin += str(secondb & 1)
    # decode messageBin with key
    decodedBin = []
    for i in range(messageLength):
        decodedBin.append(str(int(messageBin[i]) ^ int(key[i % len(key)])))
    decodedBin = "".join(decodedBin)
    new_message = "".join([chr(int(decodedBin[i:i+8], 2)) for i in range(0, len(decodedBin), 8)])
    return new_message


def makeKey(img):
    pix = img.load()
    width, height = img.size

    firstRpixs = []
    lastRpixs = []
    # the r value of beginning 64 pixel bytes moving diagonally (after random num 27) will be used to reference different rows of last 64 pixels' r values
    for i in range(27, (64 * 8) + 27):
        r, g, b = pix[i, i]
        firstRpixs.append(str(r & 1))
    # the r value of end 64 pixels moving diagonally (after random num 32) will be used to reference different rows of last 64 pixels' r values
    references = [int("".join(firstRpixs[i:i+8]), 2) for i in range(0, len(firstRpixs), 8)]
    for byte in references:
        # get the r value of the last pixs referenced (y / 3)
        r, g, b = pix[(width - 1 - byte), (height - 1 - (byte / 3))]
        lastRpixs.append(str(r & 1))
    
    key = "".join(lastRpixs)
    return key

# img = Image.open('test.png') # actually should just take img from user
# img.save("testCopy.png")
# img = Image.open("testCopy.png")
# key = makeKey(img)
# encodedImg = hide_message('test.JPG', "I really miss you! Please come home...")
# new_img = Image.open("hidden.png")
# new_key = makeKey(new_img)
# new_message = show_message('hidden.png')
# # new_key2 = makeKey(encodedImg)
# # new_message2 = show_message(encodedImg, new_key2)
# print(img==new_img)
# pass