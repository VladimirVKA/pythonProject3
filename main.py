import validator_script
import validator_sort
from time import time

if __name__ == '__main__':
    print('nice')
    validator = validator_script.Validator()

    validator.load('C:/Users/Admin/Downloads/12.txt')
    valid = validator.validate()
    validator_script.write('valid.txt', valid)
    x = time()
    sorted_valid = validator_sort.quick_sort(valid)
    print(f'{time() - x}')
    validator_sort.write('sorted_valid.txt', sorted_valid)

