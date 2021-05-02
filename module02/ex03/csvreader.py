import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        
    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
        except IOError:
            print("ERROR: \"{}\" file doesn't exist".format(self.filename))
            exit() 
        self.lines = self.file.read().split("\n")
        l = len(self.lines)
        if self.skip_top > l:
            return None
        r_l = []
        i = 0 + self.skip_top
        while i < len(self.lines) - self.skip_bottom:
            r_l.append(self.lines[i].split(self.sep))
            if len(r_l[0]) != len(r_l[i]):
                return None
            i += 1
        self.lines = r_l
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        return self.lines 

    def getheader(self):
        if self.header:
            return self.lines[0]
        else:
            return None

with CsvReader("test1.csv", header=True) as f:
    data = f.getdata()
    header = f.getheader()
    print(header)