import platform,os
#####
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    import mn
elif bit == '32bit':
    print("SORRY BRO")
