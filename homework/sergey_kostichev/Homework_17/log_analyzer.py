import argparse
import os


def check_path(directory, logs_list):
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

    for file in files:
        if file.endswith('.log'):
            file_path = os.path.join(directory, file)
            logs_list.append(file_path)
    if len(logs_list) == 0:
        print(f"There are no logs in {directory}")
        return False

    return True


def find_text_in_logs(log_files, keytext, size, short=False):
    result_logs = []
    for log_file in log_files:
        with open(log_file, 'r') as opened_file:
            line_number = 1
            for line in opened_file:
                if keytext.lower() in line.lower():
                    words = line.split()

                    for word in words:
                        if keytext.lower() in word.lower():
                            pos = words.index(word)
                            # print("Index: ", index)
                            start = max(0, pos - size)
                            end = min(len(words), pos + size + 1)

                            output = ' '.join(words[start:end])
                            result_logs.append(f"Log: '{log_file}' \nLine: '{line_number}':\n{output}")

                            if short:
                                return result_logs

                line_number += 1
    return result_logs


parser = argparse.ArgumentParser()
parser.add_argument("path", help="absolute path to Logs directory")
parser.add_argument("-t", "--text", help="key text should be searched in Logs")
parser.add_argument("-s", "--size", type=int, default=5, help="size of line to display")
parser.add_argument("--short", help="display the first found request", action="store_true")
args = parser.parse_args()


logs = []
if check_path(args.path, logs):
    results = find_text_in_logs(logs, args.text, args.size, args.short)

    if len(results) == 0:
        print(f"{args.text} wasn't found in Logs")
    else:
        counter = 1
        for log in results:
            print(f"#{counter}", log, end="\n\n")
            counter += 1
