
def Outer():
    def Inner(Outer):
        print(Outer)
        return Inner

    return Inner(Outer)

if __name__ == "__main__":
    retObj = Outer()
    print(retObj)