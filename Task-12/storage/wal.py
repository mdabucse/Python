import json
import os


class WAL:
    def __init__(self, file_path="wal.log"):
        self.file_path = file_path

        # create file if not exists
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()

    # LOG ENTRY
    def log(self, entry):
        with open(self.file_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    # READ LOGS 
    def read_all(self):
        with open(self.file_path, "r") as f:
            return [json.loads(line) for line in f if line.strip()]

    # CLEAR LOG 
    def clear(self):
        open(self.file_path, "w").close()