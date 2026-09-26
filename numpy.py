import numpy as np
scores = np.array([50, 60, 70, 80, 90 ])
result = scores * 2 + 10
print(result)

#slicing
import numpy as np
scores = np.array([85, 72, 91, 68, 95, 88, 76])

scores[2] # 91
scores[-2] # 88
scores[1:5] #[72, 91, 68, 95]
scores[:3] # [85,72,91]
scores[4:] #[95,88,76]

students = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])

students[1,2] # 75
students[2,0] # 95
students[0,0] # 80

students[0, :] # [80, 70, 95]
students[:, 1] # [70, 85, 88]
students[:, 2] # [90, 75, 92]


