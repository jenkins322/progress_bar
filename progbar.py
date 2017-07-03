def perbar(total, current, text=""):
    print(text + str(int(current / total * 100)), "%\r", end="")


def bar(total, current, length=10, prefix="", filler="#", space=" ", oncomp="", border="[]", suffix=""):
    if len(border) != 2:
        print("parameter 'edges' must include exactly 2 symbols!")
        return None

    print(prefix + border[0] + (filler * int(current / total * length) +
                                (space * (length - int(current / total * length)))) + border[1], suffix, "\r", end="")
    if total == current and oncomp:
        print(prefix + border[0] + space * int(((length - len(oncomp)) / 2)) +
              oncomp + space * int(((length - len(oncomp)) / 2)) + border[1], suffix)
    if total == current and not oncomp:
        print(prefix + border[0] + (filler * int(current / total * length) +
                                    (space * (length - int(current / total * length)))) + border[1], suffix)
