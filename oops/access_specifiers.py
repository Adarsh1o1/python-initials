class detail:
    def __init__(self) -> None:
        self.__name="harry"

a=detail()
# print(a.__name) #cannot access directly
# print(a._detail__name) #can be accessed indirectly #NAME MANGLING
print(a.__dir__()) #from this we see all the available methods on a




