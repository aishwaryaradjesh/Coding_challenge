import re
import sys


def is_number(string):  # https://elearning.wsldp.com/python3/python-check-string-is-a-number/
    try:
        float(string)
        return True
    except ValueError:
        return False

try:
    fhandle = open('input.txt')
    text = fhandle.read()  # read entire contents of file
except OSError:
        print("Could not open/read file:", 'input.txt')
        sys.exit()

expression_list = text.split('\n')
if '' in expression_list:
    expression_list = list(filter(lambda el: el != '', expression_list))  # Remove empty lines from expression list

count = 0
index = []
variable_dict = {}

while count < expression_list.__len__():  # run until all expressions are evaluated
    for i, expression in enumerate(expression_list):
        if i not in index:  # skip expression that were already computed
            expression = re.sub('\s', '', expression)  # remove white spaces
            try:
                LHS = expression.split('=')[0]
                if LHS == '' or not(LHS.isalpha()):  # skip expressions that dont have LHS example : = 6
                    count = count + 1
                    index.append(i)
                    continue
                RHS = expression.split('=')[1]
                RHS_elements = re.split('\+', RHS)  # split RHS contents using + operator
                RHS_variables = list(filter(lambda el: el.isalpha(), RHS_elements))
                if all(x in variable_dict.keys() for x in RHS_variables):  # check if RHS variables have been evaluated
                    # RHS_integers = list(filter(lambda el: el.isnumeric(), RHS_elements)) # handles only integer string
                    RHS_integers = list(filter(lambda el: is_number(el), RHS_elements))  # handles if RHS has float also
                    RHS_integers = list(map(float, RHS_integers))  # convert numerical elements from string to float
                    RHS_integers = list(map(int, RHS_integers))  # convert numerical elements from string to integers
                    RHS_sum = 0
                    for variable in RHS_variables:
                        RHS_sum = RHS_sum + variable_dict[variable]
                    RHS_sum = RHS_sum + sum(RHS_integers)
                    variable_dict[LHS] = RHS_sum  # store evaluated variables in a dictionary
                    count = count + 1
                    index.append(i)
                else:
                    continue
            except:  # to skip expressions that are not in an expected format
                count = count + 1
                index.append(i)
                continue

variable_dict_sorted = dict(sorted(variable_dict.items(), key=lambda item: item[1], reverse=True))  # reverse sort
for key, value in variable_dict_sorted.items():
    print(key, ' = ', value)
