from PIL import Image

def process_image(image_path, key, output_path, mode):
    image = Image.open(image_path)
    output_image = Image.new(image.mode, image.size)
    pixels = image.load()
    output_pixels = output_image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            if mode == "encrypt":
                output_pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            else:
                output_pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    output_image.save(output_path)
    print(f"{mode.capitalize()}ed image saved as {output_path}")

def main():
    print("Image Encryptor / Decryptor")
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter image path: ").strip()
    key = int(input("Enter key (1-255): "))
    output_path = input("Enter output image name (e.g. result.png): ").strip()

    if mode in ["encrypt", "decrypt"]:
        process_image(image_path, key, output_path, mode)
    else:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
