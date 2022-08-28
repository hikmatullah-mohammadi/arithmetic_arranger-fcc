problems = ['32 + 398', '3801 - 2', '45 + 43', '9 + 9', '11 - 9']

def arithmetic_arranger(problems, display_solution=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  first_line = ''
  second_line = ''
  dashed_line = ''
  solution_line = ''
  
  for i in problems:
    operator = ''
    if i.find('+') > -1:
      f_operand = i.split('+')[0].strip()
      s_operand = i.split('+')[1].strip()
      operator = '+'
    elif i.find('-') > -1:
      f_operand =  i.split('-')[0].strip()
      s_operand = i.split('-')[1].strip()
      operator = '-'
    else:
      return "Error: Operator must be '+' or '-'."

    f_length = len(f_operand)
    s_length = len(s_operand)
    
    if f_length > 4 or s_length > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      a = int(f_operand) == int(s_operand)
    except ValueError as err:
      return 'Error: Numbers must only contain digits.'
    
    # concatenate the operans, operator and the solution
    first_line += "      " + (f_operand if f_length >= s_length else (s_length - f_length) * ' ' + f_operand)
    second_line += "    " + operator + " " + (s_operand if s_length >= f_length else (f_length - s_length) * ' ' + s_operand)
    dashed_line += "    " + ((f_length+2) * '-' if f_length >= s_length else (s_length+2) * '-')
    # solution line
    if (display_solution):
      answer = str(int(f_operand) + int(s_operand) if operator == '+' else int(f_operand) - int(s_operand))
      solution_line += "    " + ("   " + answer if (len(answer) < f_length or len(answer) < s_length) else ("  " + answer if (len(answer) == f_length or len(answer) == s_length) else " " + answer))

  return first_line[4:] + "\n" + second_line[4:] + "\n" + dashed_line[4:] + ("\n" + solution_line[4:] if display_solution else '')

arranged = arithmetic_arranger(problems, True)
print(arranged)