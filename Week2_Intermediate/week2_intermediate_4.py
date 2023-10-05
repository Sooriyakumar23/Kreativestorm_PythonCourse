def week2_intermediate_4(file_name_with_path):
    with open(file_name_with_path, 'r') as f4:

        content4 = f4.read().split('\n')

        sum_of_numbers = 0
        for number in content4:
            sum_of_numbers += float(number)

        print('sum of all the numbers in the file', sum_of_numbers)


week2_intermediate_4('./week2_4.txt')