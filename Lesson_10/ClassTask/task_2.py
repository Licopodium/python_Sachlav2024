names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]

# Вывести длину каждого имени
name_lengths = list(map(lambda name: len(name), names))
print(name_lengths)  # Результат: [4, 3, 5, 5, 3, 5]

# Вывести только имена, длина которых больше 4
filtered_names = list(filter(lambda name: len(name) > 4, names))
print(filtered_names)  # Результат: ["Aviva", "Ronen", "Galit"]
