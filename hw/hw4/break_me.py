def exhibit_name_error():
    print(foo)

def exhibit_type_error():
    print(3 / "a")

def exhibit_attribute_error():
    foobar = 10
    print(foobar.upper())

exhibit_name_error()
exhibit_type_error()
exhibit_attribute_error()
