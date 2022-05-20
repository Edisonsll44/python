
def make_repeater_of(number_repeat):
    def repeater(string):
        assert type(string) == str, "Solo puede usar cadenas"
        return string * number_repeat
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Eddy"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Te amo Dios"))

def make_division_by(n):
    def division_clousure(dvd):
        assert type(dvd) == int, "Solo se acepta números"
        return dvd/n
    return division_clousure

def run_division():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))




if __name__ == '__main__':
    run_division()
