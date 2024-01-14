def outer():
    def inner():
        return "This is The Inner Function"
    return inner
if __name__ == "__main__":
    retObj = outer()
    retInner = retObj()
    print(retInner)
