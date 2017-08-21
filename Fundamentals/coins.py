import random

def coin_toss():
    print "Starting the program..."
    results = {"heads" : 0, "tails" :0}
    for i in range (1, 5001):
        toss = random.randint(0,1)
        if toss == 0:
            results["heads"] += 1
            side = "head"
        else:
            results["tails"] += 1
            side = "tail"
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + side + "! ... Got " + str(results["heads"]) + " head(s) and " + str(results["tails"]) + " tail(s) so far"
    print "Ending the program, thank you!"


#print random.randint(0,1)
coin_toss()