def arithmetic_arranger(problems, answer = False ):
    # Empty lists
    list_fl,list_sl,list_op,result = [],[],[],[]
    # If Error
    if len(problems)  > 5: return 'Error: Too many problems.'

    for problem in problems:
        # Treating input
        pack = problem.split()
        first_number = pack[0]
        second_number = pack[2]
        operator = pack[1]
        acepted_operators = ('+','-')
        # If Error
        if operator not in acepted_operators:
            return "Error: Operator must be '+' or '-'."
        # If Error
        if not first_number.isnumeric() or not second_number.isnumeric():
            return "Error: Numbers must only contain digits."
        # If Error
        if  len(first_number) > 4 or  len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        # Populating lists
        list_fl.append(first_number)
        list_op.append(f'{operator} ')
        list_sl.append(second_number)
        result.append(int(first_number) + int(second_number) \
               if operator == "+" else int(first_number)-int(second_number))
    #Empty Strings
    first_line, second_line, dash_line, result_line= '','','',''

    for f,s,o,r in zip(list_fl,list_sl,list_op,result):
        # Treating data and creating the strings
        l1,l2 = len(f),len(s)
        n = l1 - l2
        len_dash = len(o  + f'{ (n * " ") + s}    ')
        firstliner = f'{2 * " " + f}    ' if  l1 >= l2 else f'{(len_dash - 4 - l1) * " " + f}    '
        first_line += firstliner
        second_line += o  + f'{ (n * " ") + s}    '
        dash_line += f'{(len_dash - 4) * "-" }    '
        result_line += f'{ ((len_dash - 4) - len(str(r))) * " " }{r}    '
    # Editing Output
    r_line = result_line
    if answer:
        a_p = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip() + '\n' + r_line.rstrip()
    else:
        a_p = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()
    return a_p



# problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
# teste = arithmetic_arranger(problems, answer = True )
# print(teste)

#    32         1      45      123
# - 698    - 3801    + 43    +  49
# -----    ------    ----    -----
#  -666     -3800      88      172
#
#    32         1      45      123\n
# - 698    - 3801    + 43    +  49\n
# -----    ------    ----    -----\n
#  -666     -3800      88      172
