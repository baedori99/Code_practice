import sys
N  = int(sys.stdin.readline())
stack = []

for _ in range(N):
    stack_command = sys.stdin.readline().split()

    if (stack_command[0] == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif (stack_command[0] == "size"):
        print(len(stack))
    elif (stack_command[0] == "empty"):
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    elif (stack_command[0] == "top"):
        if (len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(stack_command[1])