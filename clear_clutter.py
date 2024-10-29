import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())

files = os.listdir("Exercises/clutteredFolder")

count = 0
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Exercises/clutteredFolder/{file}", f"Exercises/clutteredFolder/{count}.png")
        count+=1