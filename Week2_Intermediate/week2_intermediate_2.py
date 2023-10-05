def week2_intermediate_2(file_name_with_path):
    with open(file_name_with_path, 'r') as f2:

        content2 = f2.read().split('\n')

        dict = {}

        for index, line in enumerate(content2):
            dict[index+1] = line

        print (dict)

week2_intermediate_2('./week2_2.csv')