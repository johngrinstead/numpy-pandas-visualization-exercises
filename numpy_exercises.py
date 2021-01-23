import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

## 1. How many negative numbers are there?

negative_numbers = a[a < 0]

len(negative_numbers)


## 2. How many positive numbers are there?

positive_numbers = a[a > 0]

len(positive_numbers)


## 3. How many even positive numbers are there?

positive_even_numbers = positive_numbers[positive_numbers % 2 == 0]

len(positive_even_numbers)


## 4. If you were to add 3 to each data point, how many positive numbers would there be?

plus_three = a + 3

plus_three_positive = plus_three[plus_three > 0]

len(plus_three_positive)


## 5. If you squared each number, what would the new mean and standard deviation be?

squared = a ** 2

squared.mean(), squared.std()


## 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

centered_values = a - a.mean()

centered_values.mean()


## 7. Calculate the z-score for each data point. Recall that the z-score is given by:

z = (a - a.mean()) / a.std()

z


