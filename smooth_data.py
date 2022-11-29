fuel_rate_incoming = [3.0, 0.5, 10.0, 11.8, 2.1, 20.2, 3.6, 2.1, 7.0, 15.4, 12.8, 17.6, 4.3, 5.2, 1.4, 6.7, 20.4, 11.4, 18.4, 2.3, 6.6, 8.0]


fuel_rate_queue = []
max_size = 9

for x in fuel_rate_incoming:
    if len(fuel_rate_queue) >= max_size:
        fuel_rate_queue.pop()
        fuel_rate_queue.insert(0, x)
    else:
        fuel_rate_queue.insert(0, x)

    print(sum(fuel_rate_queue) / len(fuel_rate_queue))
