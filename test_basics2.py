def diamond(size):
  for i in range(1, size + 1):
    for j in range(1, size - i + 1):
      print(end = ' ')
    for k in range(1, 2 * i):
      if k == 1 or k == i * 2 - 1:
        print('*', end = '')
      else:
        print(' ', end = '')
    print()
  for i in range(size - 1, 0, -1):
    for j in range(1, size - i + 1):
      print(' ', end = '')
    for k in range(1, 2 * i):
      if k == 1 or k == i * 2 - 1:
        print('*', end = '')
      else:
        print(' ', end = '')
    print()