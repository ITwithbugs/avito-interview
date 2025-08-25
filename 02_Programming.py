# Задача N1
def returnTickets(tickets):
    # создаём словарь вида: откуда -> куда
    graph = {t["from"]: t["to"] for t in tickets}
    
    # найдём старт: тот "from", которого нет среди "to"
    all_from = set(t["from"] for t in tickets)
    all_to = set(t["to"] for t in tickets)
    start = (all_from - all_to).pop()
    
    # восстанавливаем маршрут
    route = []
    current = start
    while current in graph:
        next_city = graph[current]
        route.append({"from": current, "to": next_city})
        current = next_city
    
    return route


# Пример
tickets = [
    { 'from': 'London', 'to': 'Moscow' },
    { 'from': 'NY', 'to': 'London' },
    { 'from': 'Moscow', 'to': 'SPb' },
]

print(returnTickets(tickets))

# Задача N2
# Дано 2 отсортированных (по возрастанию) массива A и B длины M и N.  
# Нужно слить их в один отсортированный (по возрастанию) массив,  
# состоящий из элементов первых двух.  

def merge_sorted_arrays(A, B):
    i, j = 0, 0
    merged = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    # Добавляем оставшиеся элементы
    if i < len(A):
        merged.extend(A[i:])
    if j < len(B):
        merged.extend(B[j:])

    return merged


# Пример
A = [1, 2, 5]
B = [1, 2, 3, 4, 6]
print(merge_sorted_arrays(A, B))  
# Ожидаемый вывод: [1, 1, 2, 2, 3, 4, 5, 6]
