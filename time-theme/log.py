from datetime import datetime


class Log:
    def __init__(self, filename, should_log_to_file=False):
        self.filename = filename
        self.should_log_to_file = should_log_to_file

    def log(self, message):
        line = f'{datetime.now()} {message}'
        print(line)
        if self.should_log_to_file:
            with open(self.filename, 'a') as file:
                file.write(line + '\n')
