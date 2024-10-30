from os import system

list = ['yo waassup!', 'Riya', 'Dev', 'Rohan', 'shivangi', 'ok thats it']

for item in list:
    if item == list[-1] or item == list[0]:
        system(f'say {item}')
        continue
    system(f'say Hi {item}')