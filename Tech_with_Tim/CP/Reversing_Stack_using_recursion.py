stack = []


def insert_to_bottom(s, item):
    if is_empty(s):
        push(s, item)
    else:
        temp = pop(s)
        insert_to_bottom(s, item)
        push(s, temp)


def reverse(s):
    if not is_empty(s):
        temp = pop(s)
        reverse(s)
        insert_to_bottom(s, temp)


def is_empty(s):
    return len(s) == 0


def push(s, item):
    s.append(item)


def pop(s):
    if is_empty(s):
        print("Stack Underflow ")
        exit(1)

    return s.pop()


def output(text, s):
    print(text, *s)


push(stack, 4)
push(stack, 3)
push(stack, 2)
push(stack, 1)
push(stack, 8)
push(stack, 7)
push(stack, 10)
output("Before Reversing: ", stack)

reverse(stack)

output("After Reversing: ", stack)
