import os


def is_number(value):
    """function to check if value is a number"""
    try:
        float(value)
    except ValueError:
        return False
    return True


cwd = os.getcwd()

full_list = os.listdir(cwd)

files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
types = list(set([i.split('.')[1] for i in files_list]))
final_types = [j for j in types if not is_number(j)]

for file_type in final_types:
    if not os.path.exists(cwd + '\\' + file_type):
        os.mkdir(file_type)

for file in files_list:
    if not is_number(file.split('.')[-1]):
        from_path = os.path.join(cwd, file)
        to_path = os.path.join(cwd, file.split('.')[-1], file)
        os.replace(from_path, to_path)
