def print_key_value_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_key_value_args(a={"a": 123}, b="def", c="ghi")
