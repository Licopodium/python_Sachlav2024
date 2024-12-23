list_of_scores = list(map(int, input("Enter 3 scores: ").split()))
print(list_of_scores)

updated_list_of_scores = list(map(lambda x: x + 10, list_of_scores))
print(updated_list_of_scores)