text_to_map = "abc De FG tyu"

mapped_text = list(map(lambda x: x.upper(), text_to_map))
print(mapped_text)

list_of_grades = [50, 60, 70, 90, 40, 10]

updated_grades = tuple(map(lambda y: y + 10, list_of_grades))
print(updated_grades)