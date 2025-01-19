def print_kwarg(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwarg(name="iron man",power="good person")
print_kwarg(name="hanuman", power ="intllegent")
