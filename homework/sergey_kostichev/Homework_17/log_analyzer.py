from analyzer import Analyzer
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="absolute path to Logs directory")
    parser.add_argument("-t", "--text", help="key text should be searched in Logs")
    parser.add_argument("-s", "--size", type=int, default=5, help="size of line to display")
    parser.add_argument("--short", help="display the first found request", action="store_true")
    args = parser.parse_args()

    analyzer = Analyzer()

    if analyzer.check_path(args.path):
        results = analyzer.find_text(args.text, args.size, args.short)

        if not results:
            print(f"{args.text} wasn't found in Logs")
        else:
            for counter, log in enumerate(results, start=1):
                print(f"#{counter}", log, end="\n\n")
    else:
        print(f"{args.path} is not a valid directory.")


if __name__ == "__main__":
    main()
