import random
# print(f"{random.randint(1,99)}")
# print(f"{random.randrange(1,10,2)}")
# print(f"{random.uniform(1,100):.4f}")

colors = ["red", "green", "blue", "black", "white"]
number = list(range(1,100))
random_list = random.choice(colors) #สุ่มใน list
print(random_list)
random_3 = random.choices(colors, k=3) #สุ่มใน list ออกมา 3 อัน
print(random_3)
random_uniq = random.sample(colors, 3)
print(random_uniq)
num_shuf = random.shuffle(number)
print(number)
random.shuffle(number)
print("======================================")
print(number)


