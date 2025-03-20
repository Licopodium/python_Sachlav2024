for i in range(1,10):
    print(f"{i}.", end="  ")
    for j in range(1, 10):
       # print(f"{i * j:4}", end="")
      print(f"{i * j}", end="\t")
    print()