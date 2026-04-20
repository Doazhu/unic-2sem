from PIL import Image, ImageDraw, ImageFont

holidays = {
    "Новый год": "new_year.jpg",
    "День рождения": "birthday.jpg",
    "8 марта": "8_march.jpg"
}

print("Доступные праздники:", ", ".join(holidays.keys()))
holiday_name = input("К какому празднику вам нужна открытка? ")

if holiday_name in holidays:
    person_name = input("Кому предназначена открытка? ")
    text_to_write = f"{person_name}, поздравляю!"

    filename = holidays[holiday_name]
    img_card = Image.open(filename)
    
    draw = ImageDraw.Draw(img_card)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font = ImageFont.load_default()

    text_color = "yellow"
    
    x = 100
    y = 30 

    draw.text(
        (x, y), 
        text_to_write, 
        fill=text_color, 
        font=font, 
        stroke_width=3, 
        stroke_fill=text_color
    )

    img_card.show()
    img_card.save("final_card.png")
    print("Открытка готова и сохранена как final_card.png!")

else:
    print("Такого праздника нет в нашем списке.")
