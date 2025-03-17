def task_1():
    # Отримання даних від користувача
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    age = float(input("Введіть вік: "))
    city = input("Введіть місто: ")
    
    # Форматування за допомогою f-strings
    result = f"{name:<10} | {age:.2f} | {city:>15}"
    print(result)

def task_2():
    # Дані про товари
    products = [
        ("Молоко", 32.5, 2),
        ("Хліб", 18.75, 1),
        ("Яблука", 45.99, 5)
    ]
    
    # Виведення таблиці
    header = "{:<20} {:>10} {:^8}".format("Назва товару", "Ціна", "Кількість")
    print(header)
    print("-" * 40)
    for name, price, quantity in products:
        print("{:<20} {:>10.2f} {:^8}".format(name, price, quantity))

def task_3():
    # Дані про студентів
    students = [
        ("Іван Петренко", 85.5, 90),
        ("Марія Іванова", 92.0, 95),
        ("Олег Сидоренко", 78.25, 85)
    ]
    
    # Розрахунок середнього балу
    avg_score = sum(student[1] for student in students) / len(students)
    
    # Виведення звіту
    print("ЗВІТ ПРО УСПІШНІСТЬ СТУДЕНТІВ")
    print("-" * 50)
    print("{:<20} {:>10} {:>15}".format("Ім'я", "Середній бал", "Відвідуваність"))
    print("-" * 50)
    for name, score, attendance in students:
        print("{:<20} {:>10.2f} {:>15}%".format(name, score, attendance))
    print("-" * 50)
    print(f"{'Середній бал групи':<20} {avg_score:>10.2f}")

# Викликати потрібну функцію для тестування
#task_1()
#task_2()
#task_3()
