import random

def brGame(player, current):
    if player == "computer":
        num = random.randint(1, 3)
        print(f"컴퓨터가 선택한 수의 개수: {num}")
    else:
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        while True:
            if not num.isdigit():
                print("정수를 입력하세요")
                num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
                continue

            num = int(num)

            if num not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력하세요")
                num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
                continue

            break

    for i in range(num):
        print(f"{player} : {current}")
        if current == 31:
            if player == "computer":
                print("player win!")
            else:
                print("computer win!")
            exit()
        current += 1

    return current


current = 1
while True:
    current = brGame("computer", current)
    current = brGame("player", current)
