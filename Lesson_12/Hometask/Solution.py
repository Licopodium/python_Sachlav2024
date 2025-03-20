class InvalidNumberError(TypeError):
    pass

def get_number_from_user():
    try:
        user_input = input("Please enter a number: ")
        num = float(user_input)

        if num < 0:
            raise ValueError("The number cannot be negative!")

    except ValueError as ve:
        print(f"Error: {ve}")
    except InvalidNumberError:
        print("Error: Input is not a valid number!")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    else:
        print(f"Success! You entered a valid positive number: {num}")
    finally:
        print("Execution complete.")

get_number_from_user()
