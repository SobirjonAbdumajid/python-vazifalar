from functions_of_game import think_number, find_comp_number, finding_your_number,compare_of_attempts

result1 = think_number()
result2 = find_comp_number(result1)
result3 = finding_your_number()

compare_of_attempts(result3,result2)

while True:
        response = input('Wonna play again? (yes/no): ').lower()
        if response == 'yes':
            result1 = think_number()
            result2 = find_comp_number(result1)
            result3 = finding_your_number()

            compare_of_attempts(result3,result2)
        elif response == 'no':
            break
        else:
            print('Enter just yes/no!')
