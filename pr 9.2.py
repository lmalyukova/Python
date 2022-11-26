def sort_matrix_by_k(matrix, k):
  new_matrix = [[] for _ in range(len(matrix))]

  sort_order = get_sort_order(matrix, k)

  for row in range(len(matrix)):
    for column in sort_order:
      new_matrix[row].append(matrix[row][column])

  return new_matrix


def get_sort_order(matrix, k):
  sort_row = list(matrix[k - 1])
  sort_order = []

  for i in range(len(sort_row)):
    min_n = sort_row[i]
    min_n_indice = i

    for j in range(len(sort_row)):
      if sort_row[j] < min_n:
        min_n = sort_row[j]
        min_n_indice = j

    sort_order.append(min_n_indice)
    sort_row[min_n_indice] = float('inf')
  
  return sort_order


def read_matrix(filename="vvod.txt"):
  matrix = []

  with open(filename, 'r') as file:
    for line in file:
      matrix.append(list(map(int, line.split(' '))))

  return matrix


def write_matrix(matrix, filename="vivod.txt"):
  with open(filename, 'w') as file:
    file.writelines([' '.join(map(str, row)) + '\n' for row in matrix])


def output_matrix(matrix):
  for row in matrix:

    for number in row:
      print(number, end=' ')

    print()


def main():
  matrix = read_matrix()
  print('Your matrix: ')
  output_matrix(matrix)
  k = int(input('K: '))
  print('The answer is:')
  answer = sort_matrix_by_k(matrix, k)
  output_matrix(answer)
  write_matrix(answer)


if __name__ == '__main__':
  main()
