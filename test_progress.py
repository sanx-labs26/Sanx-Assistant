from progress import (
    create_progress_table,
    save_progress,
    get_progress
)

create_progress_table()

save_progress("Python", "Completed", 9)
save_progress("SQL", "Completed", 8)
save_progress("Machine Learning", "Learning", 6)

rows = get_progress()

for row in rows:
    print(f"Topic      : {row[0]}")
    print(f"Status     : {row[1]}")
    print(f"Score      : {row[2]}/10")
    print(f"Date & Time: {row[3]}")
    print("-" * 40)