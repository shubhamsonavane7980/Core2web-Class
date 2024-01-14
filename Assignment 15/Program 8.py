
def outer():
    def inner():
        return "Hello, Core 2 Web !"
    return inner
    print("In Outer Function")

if __name__ == "__main__":
    result = outer()()
    print(result)
