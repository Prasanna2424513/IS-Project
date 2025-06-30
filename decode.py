from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ''
    for pixel in pixels:
        for value in pixel:
            binary_data += str(value & 1)

    bytes_list = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in bytes_list:
        char = chr(int(byte, 2))
        if message.endswith("#####"):
            break
        message += char

    return message.replace("#####", "")


decoded = decode_message("output_image.png")
print("🔓 Decoded message:", decoded)
