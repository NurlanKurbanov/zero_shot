texts = []

with open('okr_text.txt', 'r') as file:
    for line in file:
        if line not in texts:
            texts.append(line)

with open('okr_text_clear.txt', 'a') as file0:
    for line in texts:
        file0.write(line)