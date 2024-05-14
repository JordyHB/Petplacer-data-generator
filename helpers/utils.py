def load_file_into_mem(path):
    with open(path) as f:
        return f.read().split()

