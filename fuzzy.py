def main():
    list1 = ["This is watever text", "Dont ask what it is", "HEY, I said dont ask", "No", "stop"]
    search_string = input("Give me what you want to search: ")
    if len(search_string) == 1:
        for i in list1:
            if search_string in list(i.lower()):
                print(i)

main()

# Criteria1: If the search string is just a single letter, the string matches if it contains that letter. It is case insensitive.
# Criteria2: If the search string contains more than 1 letter, the string matches if it contains atleast one of those letters. If it contains more than one of those letters, it should be in the same order as the search string has to match.
