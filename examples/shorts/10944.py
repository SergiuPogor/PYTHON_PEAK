# Example of using deque for efficient insertions

from collections import deque

def process_tasks(tasks):
    task_queue = deque(tasks)  # Initialize deque with tasks

    while task_queue:
        task = task_queue.popleft()  # Fast removal from the front
        print(f"Processing task: {task}")
        
        # Simulate adding a new task at the end
        if len(task_queue) < 5:
            new_task = f"Task {len(tasks) + len(task_queue) + 1}"
            task_queue.append(new_task)  # Fast addition at the back

# Sample task list
tasks = ["Task 1", "Task 2", "Task 3"]
process_tasks(tasks)  # Outputs processed tasks and adds new ones