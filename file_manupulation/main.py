
# Opening and reading files
# file = open("my_file.txt")
# content = file.read()
# print(content)

# Read and write to file
with open("my_file.txt", mode="r") as file:
    old_content = file.read()
    print(f"Old Content: {old_content}")

with open("my_file.txt", mode="a") as file:
    file.write(" is dummy text")

with open("my_file.txt", mode="r") as file:
    new_content = file.read()
    print(f"New Content: {new_content}")
