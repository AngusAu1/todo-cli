tasks = []

print("Enter your tasks. Press Enter on a blank input to finish.")
while True:
    task = input("Enter a task: ").strip()
    if not task:
        break
    tasks.append(task)
    print(f"Task added: {task}")

if tasks:
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
else:
    print("No tasks added.")
