import play #імпорт бібліотеки

play.set_backdrop("purple")

cringe = True

@play.when_program_starts #коли програма працює
def start():#
    global player, speech, speech1
    text1 = play.new_text(words='Г - гладити, З - зіграти, С - спати', x = 0, y =250, font_size = 40)
    text2 = play.new_text(words='К - кормити, П - прибирати, Пробіл - піти, В - вітати, Ж - жартувати. Спочатку привітай вихованця', x = 0, y =220, font_size = 40)
    player = play.new_image(image="Happy.png", x = 0, y = 0, size = 100)
    speech = play.new_text(words="Привіт", x = 0, y = -250, font_size = 40)
    speech1 = play.new_text(words=None, x = 0, y = -250, font_size = 40)
@play.repeat_forever# повторювати завжди(ігровий цикл)
async def do():#
    global cringe
    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.image = "Gymn.png"
        speech.words = "hello, я неко-Порошенко, привітай мене. В - вітати"
        await play.timer(2.0)
        player.image = "smile.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене шоколадкою рошен!"
        speech.font_size = 25
    if play.key_is_pressed("К") or play.key_is_pressed("к"):
        player.image = "Roshen.png"
        await play.timer(2.0)
        player.image = "View.jpg"
        speech.words = "Hallo? Ми не зможемо змінити країну, якщо не змінимо себе."
        await play.timer(2.0)
        player.image = "Like.jpg"
        speech.words = "Подивись який скарб тут є! Прибери це."
    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.image = "Horrible_poroh.jpg"
        speech.words = "Я ще раз наголошую, я абсолютно аж ніяк не переживаю про рейтинги і ніколи не переживав,"
        speech.font_size = 25
        speech.y = -200
        speech1.words = "бо тут два вибори: або ти робиш реформи, або ти піклуєшся про вибори, або про мене."
        speech1.font_size = 25
        speech1.y= -260
        await play.timer(4.0)
        speech1.hide()
        speech.y = -250
        speech.font_size = 40
        player.image = "These hands dont mug.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, зіграй зі мною. З - зіграти"
    if play.key_is_pressed("з") or play.key_is_pressed("З"):
        player.image = "Look what's on his hands.jpg"
        speech.words="Я єдиний український президент, який передав свої активи, залиш мене в спокії. c - спати"
        speech.size = 25
    if play.key_is_pressed("C") or play.key_is_pressed("c"):
        player.image = "poroshenko.jpg"
        speech.words = "Найбільш прийнятним є формат Мінських переговорів, так що не розмовляй зі мною більше"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, залиш вже мене! Ж - жартувати"
        speech.font_size = 25
    if play.key_is_pressed("Ж") or play.key_is_pressed("ж"):
        player.image = "Порошенко_сміється.jpg"
        speech.words =" То були лазні першого покоління, а це вже – 5-го покоління."
        speech.font_size = 25
        speech.y = -200
        speech1.show()
        speech1.words = " Там була тільки пральня і сушилка, а це вже п’яте покоління, уже з досвідом бойового застосування, і тут вже є все, і вже кажуть, що краще це не зробиш"
        speech1.font_size = 25
        speech1.y = -260
        cringe = False
    if play.key_is_pressed("Ж") or play.key_is_pressed("ж"):
        if joke == False:
            speech1.hide()
            speech.words = "Я втомився"
            speech.font_size = 40
            speech.y = -250

    

   
play.start_program()# запуск програми