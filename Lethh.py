import os, sys, time, ctypes, colorama, asyncio
from colorama import Fore
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#######################

# Fonksiyonlar buraya


w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX

def Temizle():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def Yüklenio():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

def Geçiş():
    Temizle()
    Yüklenio()
    Temizle()


def YüklenmeBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    Write.Print(f"\r                                       {prefix} |{bar}| {percent}% {suffix}", Colors.purple_to_blue, interval=0.000)
    if iteration == total:
        print()

items = list(range(0, 37))
l = len(items)

def Isim(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Developed By Hilal Askimmm")
    elif system == 'posix':
        sys.stdout.write(f"{_str} | Developed By Hilal Askimmm")
    else:
        pass

#######################

# Hilal Codesssd

def Menu():
    Isim(f"")
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Klavyeden girilen cümlenin kac harf ve kaç kelimeden oluştugunu ekrana yazdıran programı yapınız   
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Girilen bir sayının tek mi cift mi oldugunu yazan program yapınız   
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Kullanıcının girdigi iki sayı arasındaki büyük sayıyı bulan programı yapınız
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Girilen sayının Pozitif negatif veya sıfır olduğunu belirten program yapınız   
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Kullanıcının girdigi ayın kac gün cektigini belirten program yapınız''')
    Ders = input(f'\n\n{m}[{w}>{m}]{w} Hangi Ödevi Denemek İstersin Hilal askim yiaaaa?: ')

    if Ders == '1':
         Geçiş()
         cumle = input(f'{m}[{w}>{m}]{w} Cümleyi gir asskim: ')
         Temizle()
         YüklenmeBar(0, l, prefix='', suffix='', length=l)
         for i, item in enumerate(items):
            time.sleep(0.1)
            YüklenmeBar(i + 1, l, prefix='', suffix='', length=l)
         Geçiş()
         
         harfler = len(cumle)
         kelimeler = len(cumle.split())
         print(f'[{g}>{Fore.RESET}] Girilen cümle {harfler} harf ve {kelimeler} kelime içeriyor.')
         time.sleep(1)
         print(f'\n\n{g}Bu programda, input() fonksiyonu kullanıcının cümle veya metin girmesini sağlar.\nlen() fonksiyonu, girilen cümle veya metnin harf sayısını bulur.\nsplit() fonksiyonu, girilen cümleyi kelime dizisine dönüştürür ve len() fonksiyonu ile kaç kelime olduğunu bulur.${Fore.RESET}\n\n')
         exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Ödevlere geri dönmek icin enter bass askim bütün ödevlerini bana yaptırdın yiaaa: ')
         exit = clear()
         exit = Menu()


    if Ders == '2':
         Geçiş()
         sayi = int(input(f'{m}[{w}>{m}]{w} Bir sayı gir asskim: '))
         Temizle()
         YüklenmeBar(0, l, prefix='', suffix='', length=l)
         for i, item in enumerate(items):
            time.sleep(0.1)
            YüklenmeBar(i + 1, l, prefix='', suffix='', length=l)
         Geçiş()
         
         if sayi % 2 == 0:
             print(f'[{g}>{Fore.RESET}] Girilen sayı cift sayıdır asko')
         else:
             print(f'[{g}>{Fore.RESET}] Girilen sayı tek sayıdır asko')
         time.sleep(1)
         print(f'\n\n{g}Bu programda input() fonksiyonu, kullanıcıdan sayı girmesini istemek için kullanılır.\nint() fonksiyonu, kullanıcının girdiği değeri tam sayıya dönüştürmek için kullanılır. \nif ve else ifadeleri, sayının çift veya tek olduğunu kontrol etmek için kullanılır. \nEğer sayının 2ye bölümünden kalan 0 ise, if bloğu çalışır ve sayı çift olarak kabul edilir. \nAksi takdirde, else bloğu çalışır ve sayı tek olarak kabul edilir.{Fore.RESET}\n\n')
         exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Ödevlere geri dönmek icin enter bass askim bütün ödevlerini bana yaptırdın yiaaa: ')
         exit = clear()
         exit = Menu()

    if Ders == '3':
         Geçiş()
         sayi1 = int(input(f'{m}[{w}>{m}]{w} Birinci sayıyı gir asskim: '))
         sayi2 = int(input(f'{m}[{w}>{m}]{w} Birinci sayıyı gir asskim: '))
         Temizle()
         YüklenmeBar(0, l, prefix='', suffix='', length=l)
         for i, item in enumerate(items):
            time.sleep(0.1)
            YüklenmeBar(i + 1, l, prefix='', suffix='', length=l)
         Geçiş()
         
         if sayi1 > sayi2:
             print(f'[{g}>{Fore.RESET}] Girilen en büyük sayı: {sayi1}')
         else:
             print(f'[{g}>{Fore.RESET}] Girilen en büyük sayı: {sayi2}')
         time.sleep(1)
         print(f'\n\n{g}Bu programda, input() fonksiyonu kullanıcının sayıları girmesini sağlar.\nint() fonksiyonu, girilen sayıları tam sayıya dönüştürür. \nif ve else ifadeleri, sayi1 ve sayi2 değişkenlerinin değerlerini karşılaştırır ve büyük sayıyı belirler.{Fore.RESET}\n\n')
         exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Ödevlere geri dönmek icin enter bass askim bütün ödevlerini bana yaptırdın yiaaa: ')
         exit = clear()
         exit = Menu()


    if Ders == '4':
         Geçiş()
         sayi = int(input(f'{m}[{w}>{m}]{w} Bir sayı gir asskim: '))
         Temizle()
         YüklenmeBar(0, l, prefix='', suffix='', length=l)
         for i, item in enumerate(items):
            time.sleep(0.1)
            YüklenmeBar(i + 1, l, prefix='', suffix='', length=l)
         Geçiş()
         
         if sayi > 0:
             print(f'[{g}>{Fore.RESET}] Pozitif bir sayıdır: {sayi}')
         elif sayi < 0:
             print(f'[{g}>{Fore.RESET}] Negatif bir sayıdır: {sayi}')
         else: 
             print(f'[{g}>{Fore.RESET}] {sayi}')
         time.sleep(1)
         print(f'\n\n{g}Bu programda input() fonksiyonu, kullanıcıdan sayı girmesini istemek için kullanılır.\nint() fonksiyonu, kullanıcının girdiği değeri tam sayıya dönüştürmek için kullanılır.\nif, elif ve else ifadeleri, sayının pozitif, negatif veya sıfır olduğunu belirlemek için kullanılır.\nEğer sayı 0 dan büyük ise, if bloğu çalışır ve sayı pozitif olarak kabul edilir.\nEğer sayı 0 dan küçük ise, elif bloğu çalışır ve sayı negatif olarak kabul edilir.\nEğer sayı 0 ise, else bloğu çalışır ve sayı sıfır olarak kabul edilir.{Fore.RESET}\n\n')
         exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Ödevlere geri dönmek icin enter bass askim bütün ödevlerini bana yaptırdın yiaaa: ')
         exit = clear()
         exit = Menu()


    if Ders == '5':
         Geçiş()
         ay = int(input(f'{m}[{w}>{m}]{w} Bir ay numarası gir (1-12) asskim: '))
         Temizle()
         YüklenmeBar(0, l, prefix='', suffix='', length=l)
         for i, item in enumerate(items):
            time.sleep(0.1)
            YüklenmeBar(i + 1, l, prefix='', suffix='', length=l)
         Geçiş()
         
         if ay == 2:
             print(f'[{g}>{Fore.RESET}] Bu ay 28 veya 29 gün çeker.')
         elif ay in [4, 6, 9, 11]:
             print(f'[{g}>{Fore.RESET}] Bu ay 30 gün çeker.')
         else: 
             print(f'[{g}>{Fore.RESET}] Bu ay 31 gün çeker. Kaan gbi')
         time.sleep(1)
         print(f'\n\n{g}Bu programda input() fonksiyonu, kullanıcıdan ay numarası girmesini istemek için kullanılır.\nint() fonksiyonu, kullanıcının girdiği değeri tam sayıya dönüştürmek için kullanılır.\nif, elif ve else ifadeleri, ayın kaç gün çektiğini belirlemek için kullanılır.\nEğer ay 2 ise, if bloğu çalışır ve bu ayın Şubat olduğunu ve 28 veya 29 gün çektiğini belirtir.\nEğer ay 4, 6, 9 veya 11 ise, elif bloğu çalışır ve bu ayların 30 gün çektiğini belirtir.\nEğer ay 1, 3, 5, 7, 8, 10 veya 12 ise, else bloğu çalışır ve bu ayların 31 gün çektiğini belirtir.{Fore.RESET}\n\n')
         exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Ödevlere geri dönmek icin enter bass askim bütün ödevlerini bana yaptırdın yiaaa: ')
         exit = clear()
         exit = Menu()




Menu()