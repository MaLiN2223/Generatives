import time


class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = time.time()

    def elapsed(self, sec):
        if sec < 60:
            return str(sec) + " sec"
        elif sec < (60 * 60):
            return str(sec / 60) + " min"
        else:
            return str(sec / (60 * 60)) + " hr"

    def get_elapsed_time(self):
        elapsed = time.time() - self.start_time
        return elapsed

    def get_elapsed_time_string(self):
        elapsed = self.elapsed(self.get_elapsed_time())
        return f"Elapsed: {elapsed}"
