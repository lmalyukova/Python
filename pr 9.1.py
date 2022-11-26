def maxel(d):
    mx = []

    for row in d:
        if row == sorted(row) or row == sorted(row, reverse=True):
            mx.append(max(row))
      
    return mx


def read_matrix(filename="vvod.txt"):
  matrix = []

  with open(filename, 'r') as file:
    for line in file:
      matrix.append(list(map(int, line.split(' '))))

  return matrix


def write_answer(answer, filename="vivod.txt"):
  with open(filename, 'w') as file:
    file.writelines(' '.join(map(str, answer)))


def output_matrix(matrix):
  for row in matrix:

    for number in row:
      print(number, end=' ')

    print()


def output_answer(answer):
  for number in answer:
      print(number, end=' ')

  print()


mat = read_matrix()
print('Your matrix:')
output_matrix(mat)
answer = maxel(mat)
print('Result:')
output_answer(answer)
write_answer(answer)
