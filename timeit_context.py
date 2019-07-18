from contextlib import contextmanager
import time


@contextmanager
def timeit():
    start = time.monotonic()
    yield
    print(time.monotonic() - start)

def main():
    with timeit():
        time.sleep(2)

main()
