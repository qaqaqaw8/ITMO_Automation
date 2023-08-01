def task_1():
    a: int = 3
    b: float = 3.2
    c: str = 'three'
    d: list = [1, 2, 3]
    e: bool = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

def task_2(a) -> int:
    a = [1,2,3,5,8,13.21]
    return a[0:3]
print(a)

def task_3(b: int)-> int:
    return b*b
print(task_3(3))
