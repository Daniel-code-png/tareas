import uuid

def add_task(task_list, task_description):
    new_task = {
        "id": str(uuid.uuid4()),
        "description": task_description,
        "completed": False
    }
    task_list.append(new_task)
    return new_task
