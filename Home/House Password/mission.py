def checkio(data: str) -> bool:
    condition1 = condition2 = condition3 = False
    if len(data) < 10:
        return False
    else:
        for x in data:
            if x >= "a" and x <= "z":
                condition1 = True
            if x >= "A" and x <= "Z":
                condition2 = True
            if x >= "0" and x <= "9":
                condition3 = True
        if condition1 and condition2 and condition3:
            return True
        else:
            return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")