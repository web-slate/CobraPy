import gc

def create_garbage():
    garbage = [{} for _ in range(100000)]
    return garbage

def clean_up():
    collected = gc.collect()
    print(f"Garbage collector: collected {collected} objects.")

if __name__ == "__main__":
    create_garbage()
    clean_up()
