class Vulnerability:
    def __init__(self, name, description, rank):
        self.name = name
        self.description = description
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def increase_rank(self):
        self.rank += 1

    def decrease_rank(self):
        if self.rank > 0:
            self.rank -= 1


# Создание уязвимости
vulnerability1 = Vulnerability("SQL Injection", "Allows unauthorized access to the database.", 3)

# Создание описания уязвимости
vulnerability2 = Vulnerability("Cross-Site Scripting (XSS)", "Allows malicious script injection.", 2)

# Сравнение уязвимостей
if vulnerability1 == vulnerability2:
    print("Уязвимости имеют одинаковый ранг")
elif vulnerability1 > vulnerability2:
    print("Уязвимость 1 более опасна")
else:
    print("Уязвимость 2 более опасна")

# Повышение ранга уязвимости
vulnerability1.increase_rank()
print("Новый ранг уязвимости 1:", vulnerability1.rank)

# Понижение ранга уязвимости
vulnerability2.decrease_rank()
print("Новый ранг уязвимости 2:", vulnerability2.rank)
