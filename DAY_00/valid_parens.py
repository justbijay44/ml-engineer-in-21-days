def is_valid_parens(s):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    if len(s) <= 1:
        return False
    
    opening = []
    for bracket in s:
        if bracket not in brackets:
            opening.append(bracket)

        else:
            if opening and opening[-1] == brackets[bracket]:
                opening.pop()
            else:
                return False
            
    return len(opening) == 0
# print(is_valid_parens("({[]})"))
print(is_valid_parens("()]"))