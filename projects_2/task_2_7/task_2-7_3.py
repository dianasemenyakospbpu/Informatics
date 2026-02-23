seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for sequence in seq:
    print(f"Последовательность: {sequence}")
    print("Построчно:")
    for letter in sequence:
        print(letter)
    print()

print("Цикл выполнен")