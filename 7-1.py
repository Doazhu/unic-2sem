from PIL import Image

img = Image.open("postcard.jpg")

crop_box = (50, 50, 450, 450)

cropped_img = img.crop(crop_box)
cropped_img.save("cropped_postcard.jpg")
print("Картинка успешно обрезана и сохранена!")

