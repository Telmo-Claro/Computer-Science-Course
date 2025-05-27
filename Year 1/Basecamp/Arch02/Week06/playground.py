input = input("Book details: ").strip().split(",")
def test(**kwargs):
    for value in kwargs.values():
        print(value)
    
    
test(title = input[0], 
    author = input[1], 
    publisher = input[2], 
    pub_date = input[3])