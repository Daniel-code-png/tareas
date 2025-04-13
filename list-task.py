def list_tasks(task_list):
    for task in task_list:
        status = "Completado" if task["completed"] else "No completado"
        print(f'{task["id"]} - {task["description"]} [{status}]')
