def roman_to_int(roman):
    roman_values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    def helper(index):
        if index >= len(roman):
            return 0
        
        current = roman_values[roman[index]]

        if index + 1 < len(roman):
            next_ = roman_values[roman[index + 1]]
            if current < next_:
                return (next_ - current) + helper (index + 2)
    
        return current + helper(index + 1)

    return helper(0)


print (roman_to_int(input("escribe un numero romano : ")))
