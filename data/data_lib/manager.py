import csv
import os

DT_PATH = "data/tabs/"


class DataManager:
    def read(self, file: str):
        with open(DT_PATH + file, newline = "") as f :
            data = csv.reader(f)
            for i in data:
                yield i
    
    def writer(self, file, dt: list = None, mode: str = "w"): # dt [link, name]
        with open(DT_PATH + file, mode, newline = "") as f :
            data = csv.writer(f)
            if dt:
                data.writerow(dt)

    def write(self, *args, **kwargs):
        self.writer(mode = "w",*args, **kwargs)

    def add(self, *args, **kwargs):
        self.writer(mode = "a",*args, **kwargs)

    
    def files_list(self):
        return sorted(os.listdir(DT_PATH),
         key = lambda x:os.path.getmtime(DT_PATH + x))[::-1]
    

if __name__ == "__main__" :
    DT_PATH = "../tabs/"

    d = DataManager()
    d.files_list()
    d.add("1.csv", ["https://www.google.com", "google"])

    for i in d.read("1.csv"):
        print(i)



