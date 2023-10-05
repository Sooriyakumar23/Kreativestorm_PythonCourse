def week2_intermediate_3(file_name_with_path):
    with open(file_name_with_path, 'rb') as f3:

        content3 = f3.read()

        hex_content = ''

        for i in range(len(content3)):
            hex_content += hex(content3[i])

        with open('hex_file.txt', 'w') as f:
            f.write(hex_content)


week2_intermediate_3('./week2_3.bin')