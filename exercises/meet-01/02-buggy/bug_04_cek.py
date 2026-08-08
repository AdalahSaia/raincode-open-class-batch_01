nilai = 85

if nilai >= 60:
    grade = "D"
elif nilai >= 70:
    grade = "C"
elif nilai >= 80:
    grade = "B"
elif nilai >= 90:
    grade = "A"
else:
    grade = "E"

print("Grade:", grade)
#output: Grade: D 
#diminta Untuk nilai = 85, harusnya muncul "B"

#Perbaikan kode:
nilai = 85

if nilai <= 60:
    grade = "D"
elif nilai <= 70:
    grade = "C"
elif nilai >= 80:
    grade = "B"
elif nilai >= 90:
    grade = "A"
else:
    grade = "E"

print("Grade:", grade) #Output: Grade: B