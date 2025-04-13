def update_task(task_list, task_id, new_description):
    for task in task_list:
        if task["id"] == task_id:
            task["description"] = new_description
            return task
    return None
