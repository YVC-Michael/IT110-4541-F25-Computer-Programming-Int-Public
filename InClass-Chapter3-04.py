### The following code contains several nested if-else statements. Unfortunately, it
### was written without proper alignment and indentation. Rewrite the code and use the
### proper conventions of alignment and indentation.

#Named Constants
A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input('Give me your score: '))

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
