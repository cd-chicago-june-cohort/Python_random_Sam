def make_tuples(x):
    lst = []
    for key, value in x.iteritems():
        lst.append((key, value))
    print lst
    return lst

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

make_tuples(my_dict)