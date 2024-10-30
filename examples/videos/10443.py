import multiprocessing
import time

def worker(queue):
    while True:
        # Get task from queue
        task = queue.get()
        if task is None:
            break  # Exit if no more tasks
        # Simulate some work
        print(f'Processing {task}')
        time.sleep(1)  # Simulating time-consuming task
        print(f'Done processing {task}')

def main():
    num_workers = 4
    tasks = ['Task1', 'Task2', 'Task3', 'Task4', 'Task5']
    queue = multiprocessing.Queue()

    # Start worker processes
    workers = [
        multiprocessing.Process(target=worker, args=(queue,))
        for _ in range(num_workers)
    ]
    
    for w in workers:
        w.start()

    # Add tasks to the queue
    for task in tasks:
        queue.put(task)

    # Signal the workers to stop
    for _ in range(num_workers):
        queue.put(None)

    # Wait for all workers to finish
    for w in workers:
        w.join()

if __name__ == "__main__":
    main()