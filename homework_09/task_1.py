import csv
import argparse


def check_args():
    result = {key: value for key, value in vars(args).items()
              if key != 'o' and value is not None}
    if not result:
        print('Incorrect input')
        exit()
    return result


def map_elements():
    return {'brand': 'BRAND',
            'color': 'COLOR',
            'year': 'MAKE_YEAR',
            'fuel': 'FUEL',
            'reg_num': 'N_REG_NEW'}


def check_row(row):
    result = []
    for key, value in check_args().items():
        if row[map_elements()[key]] == value:
            result.append(True)
        else:
            result.append(False)
    return all(result)


def get_data_csv():
    with open(args.o, mode='r', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=';')
        result = []
        for row in file_reader:
            if check_row(row):
                result.append({'D_REG': row['D_REG'],
                                      'BRAND': row['BRAND'],
                                      'MODEL': row['MODEL'],
                                      'COLOR': row['COLOR'],
                                      'MAKE_YEAR': row['MAKE_YEAR'],
                                      'FUEL': row['FUEL'],
                                      'N_REG_NEW': row['N_REG_NEW']})
    return result


def get_filename() -> str:
    return f'brand-{args.brand}-year-{args.year}.csv'


def write_to_csv(polished_data):
    with open(get_filename(), mode='w', encoding='utf-8') as w_file:
        names = ['D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR', 'FUEL', 'N_REG_NEW']
        file_writer = csv.DictWriter(w_file, delimiter=';', lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(polished_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("o")
    parser.add_argument("--brand")
    parser.add_argument("--color")
    parser.add_argument("--year")
    parser.add_argument("--fuel")
    parser.add_argument("--reg_num")
    args = parser.parse_args()
    args_dict = {"brand": args.brand, "color": args.color, "year": args.year,
                 "fuel": args.fuel, "reg_num": args.reg_num}


write_to_csv(get_data_csv())
