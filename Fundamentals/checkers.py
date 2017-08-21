def checkerboard():
    stars_start = True
    for line in range(8):
        if stars_start:
            print "* * * *"
            stars_start = False
        else:
            print " * * * *"
            stars_start = True


checkerboard()