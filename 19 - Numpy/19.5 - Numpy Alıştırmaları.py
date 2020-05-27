import numpy as np
# 1
result = np.array([10,15,30,45,60])

# 2
result = np.arange(5,15)

# 3
result = np.arange(50,100,5)

# 4
result = np.zeros(10)

# 5
result = np.ones(10)

# 6
result = np.linspace(0,100,5)

# 7
result = np.random.randint(10,30,5)

# 8
result = np.random.randn(10)

# 9
result = np.random.randint(10,50,15).reshape(3,5)

# 10
result = np.random.randint(10,50,15).reshape(3,5)
# result = result.sum(axis=0) # Sütunlar Toplamı
# result = result.sum(axis=1) # Satır toplamı

# 11
result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
# result = result.max() # Max
# result = result.min() # Min
# result = result.mean() # Ortalama

# 12
result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
result = result.argmax()

# 13
result = np.arange(10,20)
result = result[:3]

# 14
result = np.arange(10,20)
result = result[::-1]

# 15
# result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
# result = result[0,:]

# 16
# result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
# result = result[1,2]

# 17
# result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
# result = result[:,0]

# 18
# result = np.random.randint(10,50,15).reshape(3,5)
# print(result)
# result = result ** 2

# 19
result = np.random.randint(-50,50,15).reshape(3,5)
print(result)


resultp = result[result > 0]
resultc = resultp[resultp % 2 == 0]

print(resultc)
