class MetropolisFunc:
    def __init__(self, name: str, func):
        self.func = func
        self.display = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
