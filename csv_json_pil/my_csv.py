# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import csv


class MyCsvWriter:

    def __init__(self, f_path, header, delimiter=","):
        self.f = f_path
        self.header = header
        self.delimiter = delimiter

    def writeheader(self):
        self.writer.writerow(self.header)

    def writerow(self, data: list):
        if len(self.header) != len(data):
            raise ValueError("Column count does not match data points.")
        self.writer.writerow(data)

    def __enter__(self):
        self.csv_file = open(self.f, "w", newline="")
        self.writer = csv.writer(self.csv_file, delimiter=self.delimiter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.csv_file.close()


if __name__ == '__main__':
    writer = MyCsvWriter("test_smth.csv", ["test", "test1"], delimiter=";")

    with writer as w:
        writer.writeheader()
        writer.writerow([1, 2])
        writer.writerow([1, 2, 3])


