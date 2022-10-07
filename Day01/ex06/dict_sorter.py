def handler():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]

    new_list_of_tuples = list()
    for i in list_of_tuples:
        new_list_of_tuples.append((i[0], int(i[1])))
    output = dict(new_list_of_tuples)
    output = {k: v for k, v in sorted(output.items(), key=lambda item: item[0])}
    sorted_output = {k: v for k, v in sorted(output.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_output.items():
        print(k)
    return

def main():
    handler()
    return

if __name__ == '__main__':
    main()