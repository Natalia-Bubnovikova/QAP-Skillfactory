per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("введите сумму"))
per_cent = list(per_cent.values())

bankTKB = round(money/100*per_cent[0])
bankSKB = round(money/100*per_cent[1])
bankVTB = round(money/100*per_cent[2])
bankSBER = round(money/100*per_cent[3])

deposit = [bankTKB, bankSKB, bankVTB, bankSBER]
print("Варианты накопленных сумм:", deposit)

depositmax = max(deposit)
print("Максимальная сумма, которую вы можете заработать —" , depositmax)