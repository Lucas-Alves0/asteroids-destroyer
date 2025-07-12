from PIL import Image

# Abra a imagem

img = Image.open(r'C:\Users\lucas.paula_kovi\VSCodeProjects\MyOwnProjects\asteroids_destroy\assets\background\Cenario.png')

# Converta para RGB e pegue todos os pixels
pixels = img.convert('RGB').getdata()

# Pegue cores únicas e converta para hexadecimal
unique_colors = set(pixels)
hex_colors = ['%02x%02x%02x' % color for color in unique_colors]

print(hex_colors)