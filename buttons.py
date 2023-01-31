from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
          KeyboardButton(text="Ozbek tili🇺🇿"),
          KeyboardButton(text="Русский язык🇷🇺"),
       ]
    ],
    resize_keyboard=True
)
menuMain = ReplyKeyboardMarkup(
    keyboard=[
       [
          KeyboardButton(text="Ma'lumotlar📄"),
       ],
       [
          KeyboardButton(text="Xodimlar xaqida Malumot👨‍💻"),
       ],
       [
          KeyboardButton(text="Nima yordam bera olaman😇"),
       ],
       [
          KeyboardButton(text="Savollar📝")
       ],
       [
          KeyboardButton(text="Tilni ozgartirish🇷🇺")
       ]
    ],
    resize_keyboard=True
)

menuBack = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Ortga")
        ]
    ],
    resize_keyboard=True
)