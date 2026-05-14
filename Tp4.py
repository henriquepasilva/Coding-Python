def write_numbers_to_file(filename):
    content = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "",
        "66",
        "77",
        "88",
        "99",
        "cem"
    ]

    with open (filename, "w", encoding="utf-8") as f:
        for line in content:
            f.write(line + "\n")

write_numbers_to_file("ficheiro.txt")