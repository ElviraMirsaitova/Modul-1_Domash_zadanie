grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students))
sorted_students = sorted(students)
A = (grades[0])
B = (grades[1])
J = (grades[2])
K = (grades[3])
S = (grades[4])
ball_A = sum(A)/len(A)
ball_B = sum(B)/len(B)
ball_J = sum(J)/len(J)
ball_K = sum(K)/len(K)
ball_S = sum(S)/len(S)
print(ball_A, ball_B, ball_J, ball_K, ball_S)
dict = {sorted_students[0] : ball_A, sorted_students[1] : ball_B, sorted_students[2] : ball_J, sorted_students[3] : ball_K, sorted_students[4] : ball_S}
print(dict)







