from ast import literal_eval

CSV_FILEPATH = 'animations.csv'

TXT_FILEPATHS = ('test.txt', 'test_2.txt')

with open(CSV_FILEPATH, 'w') as csv_file:
    csv_file.write('id,name,rgb_values\n')
    csv_file.write('0,First,')
    animation_data = []
    for filepath in TXT_FILEPATHS:
        with open(filepath, 'r') as txt_file:
            data = txt_file.readline()
            frame = literal_eval(data)
            animation_data.append(frame)

    csv_file.write(f'{animation_data}\n')