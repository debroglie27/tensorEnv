stack = []


def sort_item_pos(s, item):
    if is_empty(s) or item < s[-1]:
        push(s, item)
    else:
        temp = pop(s)
        sort_item_pos(s, item)
        push(s, temp)


def sorting(s):
    if not is_empty(s):
        temp = pop(s)
        sorting(s)
        sort_item_pos(s, temp)


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


stack.append(30)
stack.append(-5)
stack.append(18)
stack.append(14)
stack.append(-3)
output("Before Sorting: ", stack)

sorting(stack)

output("After Sorting: ", stack)
