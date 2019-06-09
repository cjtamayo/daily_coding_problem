"""
HELPER FUNCTIONS FOR USE IN SOLUTION SCRIPTS
"""

# Timer Decorator to time main/worker f(x)

def timer(func):
    """
    Print the runtime of the decorated function
    :param func: function that we want to be timed
    :return: value of function, but prints string of how long function ran
    """
    import functools
    import time
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        if run_time > 3659:
            hours = int(run_time/3600)
            print(f"Finished {func.__name__} in {hours:.0f} hours, {(run_time-hours*3600)/60:.0f} minutes and {run_time%60:.0f} secs")
        elif run_time > 59:
            print(f"Finished {func.__name__} in {run_time/60:.0f} minutes and {run_time%60:.0f} secs")
        else:
            print(f"Finished {func.__name__} in {run_time:.2f} secs")
        return value

    return wrapper_timer
