data = [
    {
        "name": "Dwayne Johnson",
        "follower_count": 400000000,
        "description": "Actor, producer, and former professional wrestler known for his roles in action films.",
        "country": "USA"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 600000000,
        "description": "Portuguese professional footballer widely regarded as one of the greatest players of all time.",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 330000000,
        "description": "Singer, songwriter, and actress known for her powerful vocals and successful music career.",
        "country": "USA"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 350000000,
        "description": "Reality TV star, entrepreneur, and social media personality famous for her family’s show and beauty line.",
        "country": "USA"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 450000000,
        "description": "Argentine professional footballer regarded as one of the best football players in history.",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 250000000,
        "description": "Singer, actress, and producer known for her music career and roles in TV and film.",
        "country": "USA"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 380000000,
        "description": "Reality TV star, model, and founder of the beauty brand Kylie Cosmetics.",
        "country": "USA"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 400000000,
        "description": "Singer-songwriter known for her narrative-driven music and massive success across multiple genres.",
        "country": "USA"
    },
    {
        "name": "Beyoncé",
        "follower_count": 290000000,
        "description": "Singer, songwriter, and actress widely recognized for her powerful voice and contributions to music and culture.",
        "country": "USA"
    },
    {
        "name": "Shakira",
        "follower_count": 210000000,
        "description": "Colombian singer, dancer, and philanthropist known for her global music hits and charity work.",
        "country": "Colombia"
    }
]

import random
print("HIGHER \n OR \n LOWER \n ")

def format_data(account):
    acc_name=account["name"]
    acc_descr=account["description"]
    acc_country=account["country"]
    return f"{acc_name} ,a {acc_descr} , from {acc_country}"

def check_answer(user_guess,a_follower,b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

score=0
game_should_continue = True
acc_b=random.choice(data)

while game_should_continue:
    acc_a = acc_b
    acc_b=random.choice(data)

    if acc_a == acc_b:
        acc_b=random.choice(data)

    print(f" Compare A: {format_data(acc_a)}.")
    print("VS")
    print(f" Against B: {format_data(acc_b)}.")

    guess=input("Who has more Followers: Type 'a' or 'b':").lower()

    a_follower_count=acc_a["follower_count"]
    b_follower_count=acc_b["follower_count"]

    is_correct= check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"You are Right, Current Score: {score}")
    else:
        print(f"You are Wrong, Final Score: {score}")
        game_should_continue=False
