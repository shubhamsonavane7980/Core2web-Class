
def outer(flag):
    def inner():
        return "This Is True."if flag else "This Is False"
    return inner

if __name__ == "__main__" :
    true_Function = outer(True)
    false_function = outer(False)

    print(true_Function())
    print(false_function())