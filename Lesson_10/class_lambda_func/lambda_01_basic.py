def print_hello(name: str):
    print("hello", name)

print_hello("Alex")

call_lambda = lambda name: print("hello", name.capitalize())

call_lambda("alexander")