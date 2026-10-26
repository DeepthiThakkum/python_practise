def greet(first_name, last_name):
    print(f"Hi {first_name},{last_name}")
    print("Welcome aboard")


greet("Deepthi", "Thakkum")
greet("John", "Smith")
print(greet("Deepthi", "Thakkum"))


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Deepthi")
print(message)
print(get_greeting("Deepthi"))
