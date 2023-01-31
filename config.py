from aiogram import types, Bot, Dispatcher, executor
from data import Api_Token
from buttons import asosiy_menu, menuMain, menuBack, menuMene, menuKoz, menuizi


bot = Bot(token=Api_Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message:types.Message):
    await message.answer("Этот бот помогает дарить больше улыбок детям.\nДобро пожаловать в десткий хоспис Taskin.🥳",reply_markup=asosiy_menu)

@dp.message_handler(text="Ozbek tili🇺🇿")
async def ozbek_tili_handler(message:types.Message):
    await message.answer("kerakli bolimni tanlang.",reply_markup=menuMain)

@dp.message_handler(text="Русский язык🇷🇺")
async def русский_язык_handler(message:types.Message):
    await message.answer("Выберите информацию который вам нужен.")

@dp.message_handler(text="Ma'lumotlar📄")
async def русский_язык_handler(message:types.Message):
    await message.answer_photo("https://t.me/python_9_00/600")
    await message.answer_photo("https://t.me/python_9_00/600","Ko'proq malumot:https://ezguamal.org/taskin/",reply_markup=menuBack)
    
@dp.message_handler(text="Ortga↩️")
async def русский_язык_handler(message:types.Message):
    await message.answer("Menuga otish uzhun ortga ni bosing.",reply_markup=menuMain)


@dp.message_handler(text="Xodimlar xaqida Malumot👨‍💻")
async def русский_язык_handler(message:types.Message):
    await message.answer("Bizning xodimlar.",reply_markup=menuMene)    
    
@dp.message_handler(text="Bo'lim mudiri🤵🏼‍♀️")
async def русский_язык_handler(message:types.Message):  
    await message.answer_photo("https://t.me/RespublikaZavxozlariGulirux/20042","🤵🏼 Mamayusupov Ilxom Ravshanovich:Vrach reanimatolog, Bo'lim\nmudiri.")   

@dp.message_handler(text="Shifokor👩🏼‍⚕️")
async def русский_язык_handler(message:types.Message):  
    await message.answer_photo("https://t.me/shifokorl/1810","👩‍⚕️ Yusupova Muyassar: Hamshira.")      
    await message.answer_photo("https://t.me/medikal_photos/836?single","👩‍⚕️ Nodira Shuhratovna: Katta hamshira.")
    await message.answer_photo("https://t.me/medikal_photos/832","👩‍⚕️ Ziyayeva Inoyat Dehqanovna: Vrach.")

@dp.message_handler(text="Psixolog👱🏼")
async def русский_язык_handler(message:types.Message):
    await message.answer_photo("https://t.me/markbarton_mb/950","🧑 Ochilova Zilola Absalom qizi: Psixolog.")
    
@dp.message_handler(text="Ijtimoiy xodim🤝")
async def русский_язык_handler(message:types.Message):
    await message.answer_photo("https://t.me/nogironlik/4003","🤝 Karimov Ilyos Sattorovich: Ijtimoiy xodim\nTel:+998 93 423 00 09") 

@dp.message_handler(text="Nima yordam bera olaman😇")
async def русский_язык_handler(message:types.Message):
    await message.answer("Nima Yordam bera olishim mumkin?",reply_markup=menuKoz)    

@dp.message_handler(text="Pul yordami💸")
async def русский_язык_handler(message:types.Message):
    await message.answer("Click yoki Payme orqali yordam qilishingiz mumkin.",reply_markup=menuizi)    

@dp.message_handler(text="Payme💵")
async def русский_язык_handler(message:types.Message):
    await message.answer("Summani kiriting.") 


@dp.message_handler(text="Click💵")
async def русский_язык_handler(message:types.Message):
    await message.answer("Summani kiriting.")     

@dp.message_handler(text="O'yinchoq🧸")
async def русский_язык_handler(message:types.Message):
    await message.answer("Mumkin bo'lmagan o'yinchoqlar❌.\n👉1. Yumshoq tukli o'yinchoqlar.\n👉2. Sochi bor O'yinchoqlar\\n.Mumkin bo'lgan o'yinchoqlar✅.\n👉1. Lego.\n👉2.Birgalikda bo'yaladigan raskraskalar.\n👉3.Tvister\n👉4. Qum (suniy).\n👉5. Kachela ichkariga qo'yiladigan.\\n☎️ Tel: +99870 202-00-42\n☎️ Tel: +99893 423-00-09.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)