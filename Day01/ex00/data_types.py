def data_types():
    int_var = 0
    str_var = '1'
    float_var = 2.
    bool_var = True
    list_var = [int_var, str_var, float_var, bool_var]
    dict_var = dict()
    tuple_var = tuple()
    set_var = set()

    print(f'[{type(int_var).__name__}, ' +
            f'{type(str_var).__name__}, ' +
            f'{type(float_var).__name__}, ' +
            f'{type(bool_var).__name__}, ' +
            f'{type(list_var).__name__}, ' +
            f'{type(dict_var).__name__}, ' +
            f'{type(tuple_var).__name__}, ' +
            f'{type(set_var).__name__}]')


if __name__ == '__main__':
    data_types()