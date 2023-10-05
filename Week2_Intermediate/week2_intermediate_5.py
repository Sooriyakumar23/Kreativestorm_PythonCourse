def week2_intermediate_5(file_name_with_path):
    with open(file_name_with_path, 'r') as f5:

        content5 = f5.read().split('\n')

        without_blank_content = ''

        for line in content5:
            if line == '':
                continue
            without_blank_content += line + '\n'

    with open(file_name_with_path, 'w') as f:
        f.write(without_blank_content[:-1])


week2_intermediate_5('./week2_5.txt')