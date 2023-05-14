import play #імпорт бібліотеки

play.set_backdrop("purple")



@play.when_program_starts #коли програма працює
def start():#
    text1 = play.new_text(words='Г - гладити, З - зіграти, С - спати', x = 0, y =250, font_size = 40)
    text2 = play.new_text(words='К - кормити, П - прибирати, Пробіл - піти', x = 0, y =220, font_size = 40)
    play.new_image(image="Happy.png", x = 0, y = 0, size = 100)
@play.repeat_forever# повторювати завжди(ігровий цикл)
def do():#
    pass#

   
play.start_program()# запуск програми