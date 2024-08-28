grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students= sorted(students)
#print(students)
average_score = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
#print(average_score)
zipped  = zip(students, average_score) # zip() функция объединяет элементы нескольких последовательностей (`списков`, множеств, кортежей и т.д.) в кортежи
students_grades = dict(zipped)#Для создания словаря из списков и множеств нужно сначала объединить элементы в кортежи при помощи функции zip(), а затем создать словарь из этих кортежей при помощи функции dict()
print(students_grades)