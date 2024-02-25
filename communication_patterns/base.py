

class Base:
    def __init__(self):
        pass

    def processRawName(self, raw_name):
        end_index = len(raw_name)-1
        i = end_index-1
        while raw_name[i] != "/" and raw_name[i] != "'":
            i -= 1
        
        start_index = i+1
        name = raw_name[start_index:end_index]
        # print("Name: ", name)
        return name