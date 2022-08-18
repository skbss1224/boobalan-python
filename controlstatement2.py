#training session

skill=input("tell us skill set you wish to get trained:")
timing=float(input("tell us timing you wish:"))
if timing>10.00 and timing<12.30:
    if skill=="java"or skill=="spring":
        print(skill,"training happenning cse block")
    else:print(skill,"not available in",timing)
elif skill=="python" or skill=="flask":
    if timing>13.00 and timing<16.40:
        print(skill,"training happenning mca block")
    else:
        print(skill,"not available in",timing)
elif skill=="django"and timing>16.00:
    if timing<20.00:
        print(skill,"training happening it block")
    else:
        print(skill,"not available in",timing)
else:print("requested",skill,"not offered by placement")