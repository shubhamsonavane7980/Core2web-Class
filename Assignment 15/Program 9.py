
def outer():
    message = "I am In Outer Function "
    def inner():
        return message
    return inner

if __name__ == "__main__" :
    inner_Function = outer()
    result = inner_Function()
    print(result)