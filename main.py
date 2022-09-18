
running = True
try:
    while running:
        hex_val = input("")
        if hex_val == "exit" or hex_val == "q" or hex_val == "quit":
            running = False
            break

        hex_val = hex_val.removeprefix("#")
        if len(hex_val) != 6:
            print("Please enter valid input")
            continue 

        hex_vals = [int(hex_val[0:2], 16), int(hex_val[2:4], 16), int(hex_val[4:6], 16)]
        print(str(hex_vals)+",")
except KeyboardInterrupt:
    print("\r                                                   ",end="")




