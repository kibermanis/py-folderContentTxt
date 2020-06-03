import os
my_list = os.listdir()
my_list.remove(os.path.basename(__file__))
with open('DIR_content.txt', mode='w') as f:
    for item in my_list:
        f.write(f" {item} \n")


