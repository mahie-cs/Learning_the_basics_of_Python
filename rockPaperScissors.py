import random

while True:
    rpc_arr: list[str] = ["Rock", "Paper", "Scissors"]
    rpc: int = random.randint(1, 3)
    print('''====== Rock, Paper, Scissiors ======
    [1] Rock
    [2] Paper
    [3] Scissors
          ''')
    while True:
        try:
            _input = int(input("Enter a number (1-3): "))
            if _input < 1 or _input > 3:
                print("Enter a number from 1 to 3")
                continue
        except ValueError:
            print("Enter an integer.")
            continue
        break
    if (_input+1) == rpc:
        print(f"Your opponent picked {rpc_arr[rpc-1]}\nYou win!")
    elif (_input-1) == rpc:
        print(f"Your opponent pcked {rpc_arr[rpc-1]}\nYou Lose!")
    else:
        print(f"Your opponent picked {rpc_arr[rpc-1]}\nDraw!")
    play: str = input("Play again? (y/n): ")
    if play.lower() != "y":
        print("Goodbye!")
        break
