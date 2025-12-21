def palindrome_find():
    for i in range(999, 99, -1):
        string_half = str(i)
        palindrome = int(string_half + string_half[::-1])
        for j in range(999, 99, -1):
            if j * j < palindrome:
                break
            
            if palindrome % j == 0:
                one = palindrome // j
                if 100 <= one <= 999:
                    print(f"{palindrome} is the largest palindrome and its two factors are {j} and {one}")
                    return 
palindrome_find()