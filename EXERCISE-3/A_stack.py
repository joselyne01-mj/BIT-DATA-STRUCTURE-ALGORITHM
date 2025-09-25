# declare the valiable that will hold the stack In MoMo, push ["StepA", "StepB", "StepC"].
MOMO_stack = []

print('The stack that hold the In MoMo, push ["StepA", "StepB", "StepC"].')
def momo_push(step):
    MOMO_stack.append(step)
    return f"Push {step} to stack."

# example import
momo_push("StepA")
momo_push("StepB")
momo_push("StepC")
print(f" the MOMO current stack are: {MOMO_stack} \n")  # Output: ['StepA', 'StepB', 'StepC']

# Undo 2.
def momo_undo(steps=2):
    undone_steps = []
    for _ in range(steps):
        if MOMO_stack:
            undone_steps.append(MOMO_stack.pop())
    return f"Undo steps: {undone_steps}"

momo_undo()
print(f" the MOMO current stack after undo : {MOMO_stack} \n")  # Output: ['StepA']

print(f"the remaining stack after undo 2 steps: {MOMO_stack}")  # Output: ['StepA']

# UR pushes ["AssignmentA", "AssignmentB", "AssignmentC"].
UR_stack = []
print('The stack that hold the UR pushes ["AssignmentA", "AssignmentB", "AssignmentC"].')
def ur_push(assignment):
    UR_stack.append(assignment)
    return f"Push: {assignment} to UR stack."
# example import
ur_push("AssignmentA")
ur_push("AssignmentB")
ur_push("AssignmentC")
print(f" \n the UR current stack are: {UR_stack} \n")  # Output: ['AssignmentA', 'AssignmentB', 'AssignmentC']

# Pop one. Which is top?
print('Pop one. Which is top?')
def ur_pop():
    if UR_stack:
        removal = UR_stack.pop()
        print (f"Pop: {removal} from UR stack at the top of stack.")
    return "UR stack is empty."
ur_pop()
print(f" the UR current stack after pop : {UR_stack} \n")  # Output: ['AssignmentA', 'AssignmentB']

# Challenge: Reverse "EDUCATION" using stack
print('Challenge: Reverse "EDUCATION" using stack')
def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
result = reverse_string("EDUCATION")
print(f'Reversed "EDUCATION" using stack: {result}')  # Output: "NOITACUDE"# Stack implementation in Python