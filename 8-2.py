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


def input_matrix():
  m = int(input('M: '))
  n = int(input('N: '))

  matrix = []

  print('Input the matrix:')

  for _ in range(m):
    matrix.append(list(map(int, input().split(' '))))

  return matrix


def output_matrix(matrix):
  for row in matrix:

    for number in row:
      print(number, end=' ')

    print()


def main():
  matrix = input_matrix()
  k = int(input('K: '))
  print('The answer is:')
  output_matrix(sort_matrix_by_k(matrix, k))


if __name__ == '__main__':
  main()
