import time 
from multiprocessing import Pool
from utilities import *

if __name__ == "__main__":
    nmbr_samples = 1e8
    nmbr_parallel_blocks = 4
    pool = Pool(processes=nmbr_parallel_blocks)
    nmbr_samples_per_worker = nmbr_samples / nmbr_parallel_blocks
    print(f"Samples per worker {nmbr_samples_per_worker}\n\n")

    nmbr_trials_per_process = [nmbr_samples_per_worker] * nmbr_parallel_blocks

    print("Multiprocess version:")
    t1 = time.time()
    nbr_in_quarter_unit_circles = pool.map(monte_carlo_hits_numb, nmbr_trials_per_process)
    pi_estimate = sum(nbr_in_quarter_unit_circles) * 4 / float(nmbr_samples)
    print(f"Estimated pi {pi_estimate}")
    print(f"Time delta: {time.time() - t1}")

    print("\n\nOne process version: ")
    t1 = time.time()
    hits = monte_carlo_hits_numb(nmbr_samples)
    pi_estimate = hits * 4 / float(nmbr_samples)
    print(f"Estimated pi {pi_estimate}")
    print(f"Time delta: {time.time() - t1}")

    print("\n\nMultiprocess version - numpy:")
    t1 = time.time()
    nbr_in_quarter_unit_circles = pool.map(numpy_monte_carlo_hits_numb, nmbr_trials_per_process)
    pi_estimate = sum(nbr_in_quarter_unit_circles) * 4 / float(nmbr_samples)
    print(f"Estimated pi {pi_estimate}")
    print(f"Time delta: {time.time() - t1}")

    print("\n\nOne process version - numpy: ")
    t1 = time.time()
    hits = numpy_monte_carlo_hits_numb(nmbr_samples)
    pi_estimate = hits * 4 / float(nmbr_samples)
    print(f"Estimated pi {pi_estimate}")
    print(f"Time delta: {time.time() - t1}")