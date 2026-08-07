from database import init_db
from task_manager import (
    create_task,
    list_tasks,
    finish_task,
    remove_task
)
from commands import handle_task_command

print (handle_task_command("show my task"))


init_db()

print(create_task("Study Python", "Practice OOP", "2026-07-30"))
print(create_task("Build SanX", "Complete Week 6", "2026-07-30"))

print(list_tasks())

print(finish_task(1))

print(list_tasks())

print(remove_task(2))

print(list_tasks())