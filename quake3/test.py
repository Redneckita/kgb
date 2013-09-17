import math, re



GEARS = [
  ['nade', 1, True]
  ,['snipers',2,True]
  ,['spas',4,True]
  ,['pistols',8,True]
  ,['automatic',16,True]
  ,['negev',32,True]
]

gearCounter = math.pow(2,len(GEARS))-1
print 'initial gear: ' + str(int(gearCounter))

while True:
    command = raw_input('select weap: ')
    print command
    value = ''
    if command.startswith("+"):
        param = "+"
        value = re.findall(r'[+-](\w+)', command)[0]
        print param, value
    elif command.startswith("-"):
        param = "-"
        value = re.findall(r'[+-](\w+)', command)[0]
        print param, value
    for i in range(0,len(GEARS)):
        if GEARS[i][0] == value:
            if param == "+":
                GEARS[i][2] = True
                print GEARS[i][0]
            else:
                GEARS[i][2] = False
                print GEARS[i][0]
    if command in ["all", "none"]:
        for i in range(0,len(GEARS)):
            if command=="all":
                GEARS[i][2] = True
            else:
                GEARS[i][2] = False

    print GEARS
    gearCounter = math.pow(2,len(GEARS))-1
    print gearCounter
    for i in range(0,len(GEARS)):
        if not GEARS[i][2]:
        #     gearCounter += GEARS[i][1]
        # else:
            gearCounter -= GEARS[i][1]
    print 'gear is:' + str(int(gearCounter))