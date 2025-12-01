MAX_DIAL=100

dial = 50
hit_zero = 0

with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        value = int(line[1:])
        
        if line.startswith('L'):
            start = dial
            end = dial - value
            hit_zero += ((start - 1) // 100) - ((end - 1) // 100)
            dial = end
        else:
            start = dial
            end = dial + value
            hit_zero += (end // 100) - (start // 100)
            dial = end

print(hit_zero)