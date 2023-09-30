def arithmetic_arranger(problems, res=False):
  arranged_problems = ''
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems

  # Split the elements of the list into another list
  temp_list = []
  for string in problems:
    new_list = string.split()
    temp_list.append(new_list)

  # Check the operators.
  allowed_operators = ['+', '-']
  operators = [row[1] for row in temp_list]
  for operator in operators:
    if operator not in allowed_operators:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems

  # Check the operands
  operands = [[row[0], row[2]] for row in temp_list]
  for row in operands:
    for i in range(len(row)):
      if not row[i].isdigit():
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems
      if len(row[i]) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

  top_row = ''
  dashes = ''
  bottom_row = ''
  solutions = ''

  for row in temp_list:
    for i in range(len(row)):
      space_width = max(len(row[0]), len(row[2])) + 2
      upper = row[0].rjust(space_width)
      bottom = row[2].rjust(space_width - 1)
      dash = '-' * space_width
      signs = row[1]
      if signs == '+':
        result = int(row[0]) + int(row[2])
      if signs == '-':
        result = int(row[0]) - int(row[2])
      result = (str(result)).rjust(space_width)
    solutions += result
    top_row += upper
    dashes += dash
    bottom_row += signs + bottom

    top_row += ' ' * 4
    dashes += ' ' * 4
    bottom_row += ' ' * 4
    solutions += ' ' * 4

  if res:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
  else:
    arranged_problems = '\n'.join((top_row, bottom_row, dashes))
  return arranged_problems
