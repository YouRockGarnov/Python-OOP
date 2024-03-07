from multiprocessing import Process, Queue


def square(n, queue):
    queue.put(n * n)


def compute_squares(numbers):
    processes = []
    queue = Queue()

    for i, number in enumerate(numbers):
        process = Process(target=square, args=(number, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    return results
