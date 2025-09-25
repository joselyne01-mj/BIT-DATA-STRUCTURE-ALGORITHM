from collections import deque
# At RRA, 8 clients queue.
RRA_queue = deque()

print("At RRA, 8 clients queue.")
def rra_enqueue(client):
    RRA_queue.append(client)
    return f"Enqueue: {client} -> to RRA queue."
# example import
rra_enqueue("Client1")
rra_enqueue("Client2")
rra_enqueue("Client3")
rra_enqueue("Client4")
rra_enqueue("Client5")
rra_enqueue("Client6")
rra_enqueue("Client7")
rra_enqueue("Client8")
print(f" the RRA current queue are: {list(RRA_queue)} \n")  # Output: ['Client1', 'Client2', 'Client3', 'Client4', 'Client5', 'Client6', 'Client7', 'Client8']

# After 4 served, who is front?
print("After 4 served, who is front?")
def rra_dequeue(services=4):
    served_clients = []
    for _ in range(services):
        if RRA_queue:
            served_clients.append(RRA_queue.popleft())
    return f"Served clients: {served_clients}"
rra_dequeue()
print(f" the RRA current queue after serving 4 clients: {list(RRA_queue)} \n")  # Output: ['Client5', 'Client6', 'Client7', 'Client8']
print(f"The front client after serving 4 clients is: {RRA_queue[0]} \n")  # Output: 'Client5'

# At Airtel, 7 clients queue.
Airtel_queue = deque()
print("At Airtel, 7 clients queue.")
def airtel_enqueue(client):
    Airtel_queue.append(client)
    return f"Enqueue: {client} -> to Airtel queue."
# example import
airtel_enqueue("Client1")
airtel_enqueue("Client2")
airtel_enqueue("Client3")
airtel_enqueue("Client4")
airtel_enqueue("Client5")
airtel_enqueue("Client6")
airtel_enqueue("Client7")
print(f" the Airtel current queue are: {list(Airtel_queue)} \n")  # Output: ['ClientA', 'ClientB', 'ClientC', 'ClientD', 'ClientE', 'ClientF', 'ClientG']
print(f"The second client at Airtel is: {Airtel_queue[1]} \n")  # Output: 'ClientA'
