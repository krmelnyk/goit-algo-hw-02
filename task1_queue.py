import random
import time
from queue import Queue


# Create a queue
request_queue = Queue()

# request id counter
request_id = 0


def generate_request():
    """Generate a new request and add it to the queue."""
    global request_id
    request_id += 1

    request = {
        "id": request_id,
        "timestamp": time.time(),
        "data": f"Request data for request {request_id}",
        "priority": random.choice(["low", "medium", "high"]),
    }

    request_queue.put(request)
    print(
        f"Generated request {request_id} "
        f"with priority {request['priority']}"
    )


def process_request():
    """Process a request from the queue."""
    if not request_queue.empty():
        request = request_queue.get()
        print(
            f"Processing request {request['id']} "
            f"with priority {request['priority']}"
        )
        time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time
        print(f"Finished processing request {request['id']}")
    else:
        print("No requests to process")


def main():
    print("Starting request generator and processor...")
    for _ in range(5):
        generate_request()
        time.sleep(random.uniform(0.1, 0.5))

    while not request_queue.empty():
        process_request()


if __name__ == "__main__":
    main()
