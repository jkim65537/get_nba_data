def get_url_parameter(category, category_name):
    if not category_name:
        url_parameter = "&" + category + "="
        return(url_parameter)
    assert (isinstance(category,str)), "Category should be a string. For example, 'College'"
    assert (isinstance(category_name,str)), "Category name should be a string. For example, 'Washington'"

    category_name = category_name.replace('<', '< ')
    category_name = category_name.replace('>', '> ')

    name_list = category_name.title().split()


    #generator
    def category_name_split_generator(name_list):
        i = 0
        name_split = name_list[i]
        while True:
            yield name_split
            i += 1
            name_split = name_list[i]

    name = category_name_split_generator(name_list)

    url_parameter = "&" + category + "="  + name.__next__().replace("Vs","VS").replace("1St", "1st").replace("2Nd","2nd").replace('>', 'GT').replace('<', 'LT')
    for i in range(0, len(name_list)-1):
        url_parameter += "+"
        url_parameter += name.__next__()

    return(url_parameter)
