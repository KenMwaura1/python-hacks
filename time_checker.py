import timeit
import time 

start_time = timeit.default_timer()


# function to test time
def time_checker(x: float, y: float):
    z = x + y
    c = x * y
    d = x**2
    e = y**2
    time.sleep(5)
    return z,c,d,e
time_checker(5.8,6.9)
stop_time = timeit.default_timer()
time_elapsed_in_microseconds = (stop_time-start_time)*(10**6)
print(f"This run took {time_elapsed_in_microseconds} ms")