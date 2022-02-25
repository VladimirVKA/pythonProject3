from validator_script import Person
import tqdm as t
import json
import sys


def load(path: str = None) -> list:

    collection = []
    data = json.load(open(path, encoding='windows-1251'))
    progressbar = t.tqdm(range(len(data)))
    progressbar.set_description('Loading Person\'s data from file')
    for i in progressbar:
        temp = Person(
            data[i]['telephone'],
            data[i]['height'],
            data[i]['snils'],
            data[i]['passport_number'],
            data[i]['university'],
            data[i]['age'],
            data[i]['academic_degree'],
            data[i]['worldview'],
            data[i]['address'])
        collection.append(temp)
    print('Done')
    return collection


def write(path: str, sorted_list: list) -> None:

    result_list = []
    result_progressbar = t.tqdm(range(len(sorted_list)))
    result_progressbar.set_description('Сохраняем отсортированные записи')
    for i in result_progressbar:
        temp_dict = {'telephone': sorted_list[i].telephone,
                     'height': sorted_list[i].height,
                     'snils': sorted_list[i].snils,
                     'passport_number': sorted_list[i].passport_number,
                     'university': sorted_list[i].university,
                     'age': sorted_list[i].age,
                     'academic_degree': sorted_list[i].academic_degree,
                     'worldview': sorted_list[i].worldview,
                     'address': sorted_list[i].address}
        result_list.append(temp_dict)

    with open(path, 'w') as v_file:
        json.dump(result_list, v_file, ensure_ascii=False)


def quick_sort(list_of_persons: list) -> list:


    sys.setrecursionlimit(100000)
    if len(list_of_persons) < 2:
        return list_of_persons
    else:
        pivot = list_of_persons[0]
        less = [i for i in list_of_persons[1:] if i.age <= pivot.age]

        greater = [i for i in list_of_persons[1:] if i.age > pivot.age]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    input_path = '../valid.txt'
    output_path = '../svalid.txt'
    persons = load(input_path)

    sorted_result_list = quick_sort(persons)
    write(output_path, sorted_result_list)

    sorted_persons = load('../svalid.txt')
    for item in sorted_persons:
        print(item.age)