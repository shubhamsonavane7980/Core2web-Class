

def outer ():
    def inner():
        return  "Greetings from the inner Function"
    return inner()

if __name__ == "__main__" :
    result = outer()
    print(result)
