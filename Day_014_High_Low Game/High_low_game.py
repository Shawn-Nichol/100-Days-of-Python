import random
import game_data
import art

def select_account():
    data_length = len(game_data.data)
    num = random.randint(1, data_length)
    return game_data.data[num]

def display_account(account):
    return f"{account['name']}, {account['description']}, {account['country']}"

def compare_account(account1, account2):
    guess = input("How has more followers? Type 'A' or 'B': ").upper()
    guess_right = True

    if (guess == 'A') and (account1['follower_count'] > account2['follower_count']):
        print("You guess correctly")
    elif (guess == 'B') and (account1['follower_count'] < account2['follower_count']):
        print("You guess correctly")
    else:
        guess_right = False
        print(f"You guessed incorrectly")
    print(f"{account1['name']}, has {account1['follower_count']} followers")
    print(f"{account2['name']}, has {account2['follower_count']} followers")

    return guess_right

continue_playing = True
score = 0
while continue_playing:
    account1 = select_account()
    account2 = select_account()
    print(f"Your Score: {score}")
    print(f"Compare A: {display_account(account1)}")
    print(art.vs)
    print(f"Compare B: {display_account(account2)}")
    
    continue_playing = compare_account(account1, account2)
    score += 1
    print("\n" * 20)

print(f"GAME OVER, Your score: {score}")
