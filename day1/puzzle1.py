MAX_DIAL=100

dial = 50
hit_zero = 0

with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        value = int(line[1:])

        if line.startswith('L'):
            dial -= value
        else:
            dial += value
        
        dial %= MAX_DIAL

        if dial == 0:
            hit_zero += 1

print(hit_zero)