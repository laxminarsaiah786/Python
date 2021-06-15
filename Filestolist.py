def file(fname):
        with open(fname) as f:
                #text stores in list     
                content_list = f.readlines()
                print(content_list)

file("text.txt") 