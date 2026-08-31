# pyright: strict

def ascii_add(ascii: list[str]) -> int:
    nums: dict[str, str] = {
        "XXXX XX XX XXXX" : "0",
        " X  X  X  X  X " : "1",
        "XXX  XXXXX  XXX" : "2",
        "XXX  XXXX  XXXX" : "3",
        "X XX XXXX  X  X" : "4",
        "XXXX  XXX  XXXX" : "5",
        "XXXX  XXXX XXXX" : "6",
        "XXX  X  X  X  X" : "7",
        "XXXX XXXXX XXXX" : "8",
        "XXXX XXXX  XXXX" : "9",
        "    X XXX X    " : "-1"
    }
    answer: list[int] = []

    _ascii: list[str] = [" " + row + " " for row in ascii]
    slen: int = len(_ascii[0])
    start: int = 0
    nums_str: str = ""

    for i in range(slen+1):
        ascii_character: str = "".join((row[start:i] for row in _ascii))

        if ascii_character in nums:
            character: str = nums[ascii_character]

            if character == "-1":
                answer.append(int(nums_str))
                nums_str = ""
            else:
                nums_str += character

            start = i-1
        else:
            pass

        if i-start >= 3:
            start += i-start-2
        else:
            pass
    
    if nums_str != "":
        answer.append(int(nums_str))
    else:
        pass

    return sum(answer)