# Bug: Infinite loop due to incorrect loop condition
i = 0
while i < 10:
    print(i)
    # Missing increment: i += 1
