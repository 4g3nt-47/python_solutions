"""
TCS TQNT NINJA 2020 PROBLEM STATEMENT
DATE 08.08.2019

Given a range between M and N, you have to print all the Co-binary Palindromes.
And finally print the Amount of Co-Binary Palindromes found.
Co-Binary Palindromes are the Palindromes where Both the number and it's binary
are palindromes, for example, 313 is a palindromes and so is it's binary 100111011.
</b>Test cases:</b>
1. Take Input in one line seperated by Space.
2. if input is given 100 1000 then the final output should be 3
"""
m,n=input("Enter your range: ").split()
m=int(m); n=int(n);count =0
for i in range(m,n):
    if ((str(i) == str(i)[::-1])and(str(bin(i))[2:]==str(bin(i))[2:][::-1])):
        print(i)
        count+=1
print('total number of palindromes are ',count)
