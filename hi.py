with open("Verification Code.txt", "w") as file:
    for num in range(10000):
        code = str(num).zfill(4)
        file.write(code + "\n") 