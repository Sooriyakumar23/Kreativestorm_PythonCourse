def week2_intermediate_1(file_name_with_path):
    with open(file_name_with_path, 'r') as f1:

        content1 = f1.read()

        content_lines = content1.split('\n')

        number_of_lines = len(content_lines)
        number_of_words = len(content1.split())
        number_of_characters = 0
        for line in content_lines:
            number_of_characters += len(line)
        
        print (f'Number of lines in {file_name_with_path} =', number_of_lines)
        print (f'Number of words in {file_name_with_path} =', number_of_words)
        print (f'Number of characters in {file_name_with_path} =', number_of_characters)

week2_intermediate_1('./week2_1.txt')