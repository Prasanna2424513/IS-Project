from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_msg = ''.join([format(ord(char), '08b') for char in message + "#####"])
    pixels = list(img.getdata())

    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if msg_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    print("✅ Message encoded successfully into", output_path)


message = "Secret123"
encode_message("input_image.png", message, "output_image.png")
