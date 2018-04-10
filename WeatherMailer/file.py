def new_file(file_name, obj_type):
    file_items = []
    path = "C:\\Users\\mpeixoto\\Documents\\" + file_name
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print(obj_type + " file not found.")
        pass
    for line in file:
        file_items.append(line.strip().split(": "))
        pass
    obj_list = []
    new_obj = ""
    for item in range(len(file_items)):
        new_obj = obj_type(file_items[item][0], file_items[item][1])
        obj_list.append(new_obj)
        pass
    return obj_list
