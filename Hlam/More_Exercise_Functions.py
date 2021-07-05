def data_count(type, data):
    result = None
    if type == 'int':
        result = int(data) * 2
    elif type == 'real':
        result = float(data) * 1.5
    else:
        result = '$' + data + '$'
    return result
data_type = input()
data = input()
if data_type == 'real':
    print(f'{data_count(data_type, data):.2f}')
else:
    print(data_count(data_type, data))