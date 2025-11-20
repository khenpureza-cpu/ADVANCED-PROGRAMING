# Activity 8: All concept of OOP in Python - Tuples, Set, Linked List, Stack, Queue, Tree
student = ("John", 20, "CS")
print("Tuple:", student)
print("First element:", student[0])

fruits = {"apple", "banana", "orange"}
fruits.add("grape")
print("Fruits set:", fruits)

numbers = [10, 20, 30]
numbers.append(40)
print("List:", numbers)
print("First element:", numbers[0])

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)
popped = stack.pop()
print("Popped:", popped)
print("Stack after pop:", stack)

queue = []
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:", queue)
dequeued = queue.pop(0)
print("Dequeued:", dequeued)
print("Queue after dequeue:", queue)

person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print("Person:", person)
print("Name:", person["name"])
