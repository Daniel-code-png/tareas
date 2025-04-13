def delete_task(task_list, task_id):
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            return task
    return None
