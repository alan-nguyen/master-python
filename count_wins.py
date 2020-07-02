def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    for i in range(0, len(dice1)):
      for j in range(0, len(dice2)):
        if dice1[i] > dice2[j]:
          dice1_wins += 1
        elif dice1[i] < dice2[j]:
          dice2_wins += 1
  
    return (dice1_wins, dice2_wins)

# Test cases
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
# Expect 15, 15
print(count_wins(dice1, dice2)) 

dice1 = [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]
# Expect 16, 20
print(count_wins(dice1, dice2)) 