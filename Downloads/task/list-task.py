def list_tasks(task_list):
    for task in task_list:
        status = "✅" if task["completed"] else "❌"
        print(f'{task["id"]} - {task["description"]} [{status}]')
