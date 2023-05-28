import play #імпорт бібліотеки

play.set_backdrop("purple")



@play.when_program_starts #коли програма працює
def start():#
    global speech, player
    text1 = play.new_text(words='Г - гладити, З - зіграти, С - спати', x = 0, y =250, font_size = 40)
    text2 = play.new_text(words='К - кормити, П - прибирати, Пробіл - піти', x = 0, y =220, font_size = 40)
    player = play.new_image(image="Happy.png", x = 0, y = 0, size = 100)
    speech = play.new_text(words="Привіт", x = 0, y = -250, font_size = 40)
@play.repeat_forever# повторювати завжди(ігровий цикл)
async def do():#
    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене шоколадкою рошен!"
    if play.key_is_pressed("К") or play.key_is_pressed("к"):
        player.image = "Roshen.png"
        await play.timer(2.0)
        player.image = "View.jpg"
        speech.words = "Hallo? Ми не зможемо змінити країну, якщо не змінимо себе."
        await play.timer(2.0)
        player.image = "Like.jpg"
        speech.words = "Подивись який скарб тут є! Прибери це."
    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.image = "Horrible.poroh.jpg"
        speech.words = "Я ще раз наголошую, я абсолютно аж ніяк не переживаю про рейтинги і ніколи не переживав, бо тут два вибори: або ти робиш реформи, або ти піклуєшся про вибори, або про мене."
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, зіграй зі мною"
    if play.key_is_pressed("з") or play.key_is_pressed("З"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
    if play.key_is_pressed("й") or play.key_is_pressed("Й"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
    if play.key_is_pressed("й") or play.key_is_pressed("Й"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
    if play.key_is_pressed("й") or play.key_is_pressed("Й"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
    if play.key_is_pressed("й") or play.key_is_pressed("Й"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
    if play.key_is_pressed("й") or play.key_is_pressed("Й"):
        player.image = "Gymn.jpg"
        speech.words = "hello, я неко-Порошенко"
        await play.timer(2.0)
        player.image = "Finger.jpg"
        speech.words = "Я не хочу війни, я не прагну помсти, покорми мене"
        

    

   
play.start_program()# запуск програми