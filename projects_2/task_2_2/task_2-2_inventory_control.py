new_reagent = input('Введите название нового реагента: ')
clear_reagent = new_reagent.upper()
quantity_of_reagent = input('Введите количество реагента: ')
result = (f'Реактив {clear_reagent} поступил на склад в количестве {quantity_of_reagent} шт.')

print(result)

f = open("C:\\Users\\User\\Documents\\semenyako_dd\\projects_2\\task_2_2\\inventory.txt", 'w', encoding="utf-8")
print(result, file=f)
f.close()
