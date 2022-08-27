from __future__ import annotations
from functools import total_ordering

import os.path
import random
import re
import time
from multiprocessing import Pool, Process
from multiprocessing.dummy import Pool as ThreadPool
from unittest import result

import numpy as np
import scipy.io.wavfile

def gen_fake_data(filenames):
    print("generating fake data")
    try:
        os.mkdir("sounds")
    except FileExistsError:
        pass

def etl_demo():
    filenames = [f"sounds/example{n}.wav" for n in range(24)]
    start_t = time.perf_counter()

    print("starting etl")
    with Pool() as pool:
        results = pool.imap_unordered(etl, filenames)

        for filename, duration in results:
            print(f"{filename} completed in {duration:.2f}s")
    
    end_t = time.perf_counter()
    total_duration = end_t - start_t
    print(f"etl took {total_duration:.2f}s total")

def run_normal(items, do_work):
    print("running normally on 1 cpu")
    start_t = time.perf_counter()
    results = list(map(do_work, items))
    end_t = time.perf_counter()
    wall_duration = end_t - start_t
    print(f"it took: {wall_duration:.2f}s")
    return results

def run_with_mp_map(items, do_work, processes=None, chunksize=None):
    print(f"running using multiprocessing with {processes=}, {chunksize=}")
    start_t = time.perf_counter()
    with Pool(processes=processes) as pool:
        results = pool.map(do_work, items, chunksize=chunksize)
    end_t = time.perf_counter()
    wall_duration = end_t - start_t
    print(f"it took: {wall_duration:.2f}s")
    return result

def times_10(item):
    return item * 10

def fib(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def compare_mp_map_to_normal():
    items = list(range(1000))
    do_work = times_10
    run_with_mp_map(items, do_work)

    print()
    print(run_normal(items, do_work))

