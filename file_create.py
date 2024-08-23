import os
from faker import Faker


fileName_list = []


file_count = 3
fake = Faker()
random_words = fake.words(file_count)


for x in range(file_count):
	random_name = random_words[x][0].upper() + random_words[x][1:].lower()
	file_name = '{} - File Name - {}'.format(random_name, x)
	os.mkdir(file_name)
	fileName_list.append(file_name)

print(fileName_list)

