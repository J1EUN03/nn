import random

choices = ["가위", "바위", "보"]

computer = random.choice(choices)
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print(f"\n당신: {user}")
print(f"컴퓨터: {computer}\n")

if user == computer:
    print("비겼습니다!")
elif (user == "가위" and computer == "보") or \
     (user == "바위" and computer == "가위") or \
     (user == "보" and computer == "바위"):
    print("당신이 이겼습니다!")
else:
    print("당신이 졌습니다!")
