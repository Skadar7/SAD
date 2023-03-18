def logger(func):
    def wrapped():
        try:
            func()
        except Exception as e:
            with open('log.txt', 'w') as f:
                f.write(str(e))
    return wrapped


@logger
def summator():
    return 1 / 0

logger()