test_name = input("Enter the name of your test: ")
max_score = int(input("Enter the max score: "))
score = float(input("Enter your score: "))
percentage = round(score / max_score * 100, 2)

if percentage <= 100 and percentage >= 90:
  print("You got", percentage, "% which is an A+")
elif percentage <= 89 and percentage >= 80:
  print("You got", percentage, "% which is an A")
elif percentage <= 79 and percentage >= 70:
  print("You got",percentage,"% which is a B")
elif percentage <= 69 and percentage >= 60:
  print("You got", percentage, "% which is a C")
elif percentage <= 59 and percentage >= 50:
  print("You got", percentage, "% which is a D")
elif percentage <= 49:
  print("You got", percentage, "% which is a F")
  