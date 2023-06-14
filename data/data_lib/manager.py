import csv
import os



DT_PATH = "data/tabs/"


class DataManager:
    def read(self, file: str):
        with open(DT_PATH + file, newline = "") as f :
            data = csv.reader(f)
            for i in data:
                yield i
    
    def rewrite_file(self, original, copy):
        with open(DT_PATH + copy) as file_copy:
            with open(DT_PATH + original, "w") as original_file:
                original_file.write(file_copy.read())



    def writer(self, file, dt: tuple = (), mode: str = "w"): # dt [link, name]
        with open(DT_PATH + file, mode, newline = "") as f :
            data = csv.writer(f)
            if dt:
                data.writerows(dt)

    def clear_file(self, file):
        with open(DT_PATH + file, mode = "w") as f:
            f.write("")

    def write(self, *args, **kwargs):
        self.writer(mode = "w",*args, **kwargs)

    def add(self, *args, **kwargs):
        self.writer(mode = "a",*args, **kwargs)

    
    def files_list(self):
        listdir = os.listdir(DT_PATH)
        listdir.remove("copy")
        print(listdir)
        return sorted(listdir ,
         key = lambda x:os.path.getctime(DT_PATH + x)) #[::-1]

    def delete_file(self, file):
        os.remove(DT_PATH + file)

    def make_file(self, file_name):
        with open(DT_PATH + file_name + ".csv", "w") as f:
            f.write("")

    def __sub__(self, data):
        original_file = data[0]
        copy = "copy/" + original_file
        data_to_avoid = list(data[1:])
        self.clear_file(copy)

        for line in self.read(original_file):
            if line != data_to_avoid:
                self.add(copy, dt = (line, ) )

        self.rewrite_file(original_file, copy)
        self.delete_file(copy)


if __name__ == "__main__" :
    DT_PATH = "../tabs/"

    d = DataManager()
    d.files_list()

    #d.write("1.csv", (["https://www.google.com", "golaalgl"],))
    d.add("1.csv", [["https://www.google.com", "google"],])

    for i in d.read("2.csv"):
        print(i)



