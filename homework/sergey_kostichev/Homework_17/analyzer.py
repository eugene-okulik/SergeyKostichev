from log import Log
import os


class Analyzer:
    def __init__(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)

    def find_text(self, keytext, size, short=False):
        result_logs = []
        for log in self.logs:
            result_logs.extend(self.parse_log(log, keytext, size, short))
            if short and result_logs:
                break
        return result_logs

    def parse_log(self, log, keytext, size, short):
        results = []
        with open(log.file_path, 'r') as file:
            line_number = 1
            for line in file:
                if keytext.lower() in line.lower():
                    words = line.split()
                    for word in words:
                        if keytext.lower() in word.lower():
                            pos = words.index(word)
                            start = max(0, pos - size)
                            end = min(len(words), pos + size + 1)

                            output = ' '.join(words[start:end])
                            results.append(f"Log: '{log.get_name()}' \nLine: '{line_number}':\n{output}")

                            if short:
                                return results
                line_number += 1
        return results

    def check_path(self, directory):
        if not os.path.exists(directory):
            print(f"{directory} doesn't exist.")
            return False

        if not os.path.isdir(directory):
            print(f"{directory} is not a directory")
            return False

        files = os.listdir(directory)
        if len(files) == 0:
            print(f"There are no files in '{directory}'")
            return False

        logs_list = []
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(directory, file)
                logs_list.append(Log(file_path))

        if len(logs_list) == 0:
            print(f"There are no logs in {directory}")
            return False

        self.logs = logs_list
        return True
