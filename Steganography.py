import tkinter
from PIL import Image
from encrypt import encrypt, decrypt

def hide(path, message):
    img = Image.open(path)

    width, height = img.size
    # bits = bin(int.from_bytes(message, 'big'))[2:]
    # bits = bin(int(message, 2))[2:]
    bits = bin(int.from_bytes(message.encode(), 'big'))[2:]
    leng = len(bits)
    
    if len(bits) > width * height * 3: # and key
        raise ValueError('Message too large to hide in image.')
    
    for i in range(len(bits)):
        x = i % width
        y = i // width
        r, g, b = img.getpixel((x, y))
        r = r & ~1 | int(bits[i])
        img.putpixel((x, y), (r, g, b))
    img.save('new_img.jpeg')
    img.show()
    # TODO: hide the message in a more difficult way to find instead of just the first bits
    # TODO: mix up the channels, the image turns a different shade of red after imbedding the message
    
    
    # img = Image.new('RGB', (width, height))
        
    
    # img.show()
    # pix = img.load()
    # print(pix)
    return img

def show(path):
    img = Image.open(path)
    width, height = img.size
    message = ''
    bits = ''
    for i in range(width * height * 3):
        x = i % width
        y = i // width
        r, g, b = img.getpixel((x, y))
        bits += str(r & 1)
        if len(bits) == 8:
            byte = int(bits, 2)
            if byte == 0:
                break
            message += bits
            bits = ''
    found_message = bin(int(message, 2))[2:]
    # print(message)
    return found_message


def makeKey(path):
    img = Image.open(path)
    width, height = img.size
    total = int(width * height / 6) - 97
    collect = ''
    for i in range(total, int(total / 8), -12):
        x = i % width
        y = i // height
        r, g, b = img.getpixel((x, y))
        collect += str(g & 1)
    key = ''.join([collect[i] for i in range(0, 16 * 64, 16)])
    # TODO: Make sets of bits reference other bits to make key
    return key


key = makeKey('test.jpeg')
message = 'Hello, World!' # 64 bits
messagebin = format(int.from_bytes(message.encode(), 'big'), '064b')
encryptedMessage = encrypt(message, key)
new_img = hide('test.jpeg', encryptedMessage)

# message = show('new_img.jpeg')
new_key = makeKey('new_img.jpeg')
found_message = show('new_img.jpeg')
print(len(str(found_message)))
new_message = decrypt(found_message, new_key)
#  show(new_key, message)


print(new_message)
