friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

random_friend_num = random.randint(0,4)

print(friends[random_friend_num])

print(random.choice(friends))