import pandas as pd
data2 = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
print(data2)
# Output:
# 5 Tom
# 2 Li
# 2 Antonio
# 3 Mary
print(data2[2])
# Output:
# 2 Li
# 2 Antonio

data3 = data2.reset_index(drop=True)
print(data3)
# output:
# 0 Tom
# 1 Li
# 2 Antonio
# 3 Mary