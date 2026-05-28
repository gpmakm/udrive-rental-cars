def branch_checker(branchcode,branchname):
    n=input("Enter your regno: ")
    regno=tuple(n)
    code=tuple(branchcode)
    if regno[2] == code[0]:
        if regno[3] == code[1]:
            if regno[4] == code[2]:
                return True
    return False