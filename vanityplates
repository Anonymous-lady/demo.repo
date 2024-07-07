def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            for char in s:
                if char.isdigit():
                    position = s.index(char)

                    if s[position:].isdigit() and int(char) != 0:
                        return True
                    else:
                        return False

main()
