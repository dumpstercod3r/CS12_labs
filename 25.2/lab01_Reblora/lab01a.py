# pyright: strict

def convert(money_int: str) -> str:
    pesos_int: str = ""
    cents_int: str = ""
    money_str: str = ""

    pesos_int, cents_int = money_int.split(".")

    pesos_str: str = convert_pesos(pesos_int)
    cents_str: str = convert_cents(cents_int)

    if pesos_str == "":
        money_str += "zero pesos"
    elif pesos_str == "one":
        money_str += pesos_str + " peso"
    else:
        money_str += pesos_str + " pesos"

    if cents_str == "":
        pass
    elif cents_str == "one":
        money_str += " and " + cents_str + " centavo"
    else:
        money_str +=  " and " + cents_str + " centavos"

    return money_str

ones: list[str] = [" zero", " one", " two", " three", " four", " five", " six", " seven", " eight", " nine"]
teens: list[str] = ["0", " eleven", " twelve", " thirteen", " fourteen", " fifteen", " sixteen", " seventeen", " eighteen", " nineteen"]
tys: list[str] = ["0", " ten", " twenty", " thirty", " forty", " fifty", " sixty", " seventy", " eighty", " ninety"]

def convert_digits(digits_int: str) -> str:
    digits_str: str = ""

    lend: int = len(digits_int)

    if lend == 0:
        return ""
    elif lend == 1:
        digits_str += ones[int(digits_int)]
    elif lend == 2:
        _ones: str = digits_int[1]
        _tens: str = digits_int[0]

        if _ones != "0":
            if _tens == "1": # teens
                digits_str += teens[int(_ones)]
            else: # tys + ones
                digits_str += tys[int(_tens)] + "-" + ones[int(_ones)][1:]
        else: # tys only
            digits_str += tys[int(_tens)]
    else:
        _ones: str = digits_int[2]
        _tens: str = digits_int[1]
        _hundos: str = digits_int[0]

        digits_str += ones[int(_hundos)] + " hundred"

        if _tens != "0":
            digits_str += convert_digits(digits_int[1:])
        else:
            if _ones != "0":
                digits_str += ones[int(_ones)]
            else:
                pass
            
    return digits_str

def convert_pesos(pesos_int: str) -> str:
    pesos_str: str = ""
    hundred_places: list[str] = pesos_int.split(",")

    for p, digits in enumerate(reversed(hundred_places)):
        numba: str = convert_digits(digits.lstrip("0"))

        if numba != "":
            if p == 0:
                pesos_str += numba
            elif p == 1:
                pesos_str = numba + " thousand" + pesos_str
            elif p == 2:
                pesos_str = numba + " million" + pesos_str
            else:
                pass
        else:
            pass

    return pesos_str.strip()

def convert_cents(cents_int: str) -> str:
    lenc: int = len(cents_int)

    if lenc != 2:
        cents_int += (2-lenc)*"0"
    else:
        pass
    cents_str: str = convert_digits(cents_int.lstrip("0"))

    return cents_str.strip()