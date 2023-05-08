# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

import math
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)
sum = 0
for elem in violator_songs_list:
    if elem[0] == 'Halo' or elem[0] == 'Enjoy the Silence' or elem[0] == 'Clean':
        sum+=elem[1]
print(f'Три песни звучат {math.modf(sum)[1]} минут {round(math.modf(sum)[0]*60,0)} секунд')


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

sum3 = violator_songs_dict['Sweetest Perfection']+violator_songs_dict['Policy of Truth']+violator_songs_dict['Blue Dress']
print(f'А другие три песни звучат {math.modf(sum3)[1]} минут {round(math.modf(sum3)[0]*60,0)} секунд')