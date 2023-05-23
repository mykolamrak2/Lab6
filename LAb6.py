import math

# отримання оцінок від користувача
tasks = []
while True:
    a = float(input("Enter optimistic estimate for task (a): "))
    m = float(input("Enter most likely estimate for task (m): "))
    b = float(input("Enter pessimistic estimate for task (b): "))
    tasks.append((a, m, b))
    choice = input("Do you want to add another task? (y/n): ")
    if choice.lower() == 'n':
        break

# розрахунок оцінки та стандартного відхилення для кожного завдання
E_tasks = []
SD_tasks = []
for task in tasks:
    a, m, b = task
    E_task = (a + 4*m + b) / 6
    SD_task = (b - a) / 6
    E_tasks.append(E_task)
    SD_tasks.append(SD_task)

# розрахунок оцінки та стандартного відхилення для всього проекту
E_project = sum(E_tasks)
SE_project = math.sqrt(sum([sd**2 for sd in SD_tasks]))
CI_project_lower = E_project - 2*SE_project
CI_project_upper = E_project + 2*SE_project

# виведення результатів
print(f"Project's 95% confidence interval: {CI_project_lower:.2f} ... {CI_project_upper:.2f} points")
