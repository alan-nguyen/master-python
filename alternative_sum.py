def alter_sum(num):
  sum = 0
  for i in range(1, num):
    sum += 1/(i *(i+1))
  return sum
print(alter_sum(99))

