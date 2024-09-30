def get_valid_rating():
    while True:
        scale = input("\nOn a scale of 1 - 10 how do you feel today? (1: 😢, 10: 😊)\n")
        if scale.isdigit():
            scale = int(scale)
            if scale in range(1, 11):
                return scale
        print("Invalid entry. Please enter a valid rating from 1-10.")

def main():
    print ("Positivity Machine\n")
    name = input("\nWhat is your name?\n").capitalize()
    goal = input("\nWhat do you want to acheieve?\n").lower()
    scale = get_valid_rating()
    if scale < 4:
        print(f"\nHey {name}, keep your chin up! Today you're going to {goal} in the most amazing way, simply by being you - YOU ROCK!\n")
    elif scale >=4 and scale < 7:
        print(f"\nHey {name}, You can make a decent day a great day! Today you will {goal} and feel empowered and fulfilled by your efforts - YOU GOT THIS!\n")
    else:
        print(f"\nHey {name}, keep that positive momentum by sharing this energy! Today you will {goal} like never before - GO GET 'EM CHAMP!!\n")

main()