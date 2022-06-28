student_heights = input("Enter the heights of the students: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
avg = 0
for n in range(0, len(student_heights)):
    avg = avg + student_heights[n]
avg = avg / len(student_heights)

avg = int(avg)
print("The average height of the students is:", avg,"cm")
