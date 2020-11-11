import sys


def main(filename):
    git_log_text = ""
    with open(filename, "r") as file:
        git_log_text = file.read()

    result = process_git_log(git_log_text)
    print(result)


def process_git_log(log):
    commits = log.split("^^")

    result = "epoch,timestamp,author,file,churn_count\n"
    for number, commit in enumerate(commits):
        if commit != "":
            commit_lines = commit.split("\n")
            commit_basics = commit_lines[0]
            print(commit_basics)
            commit_basics_parts = commit_basics.split("--")
            epoch = commit_basics_parts[0]
            tmsp = commit_basics_parts[1]
            author = commit_basics_parts[2]
            total_lines = len(commit_lines)
            for row_index in range(3, total_lines - 1):
                churn_line = commit_lines[row_index]
                churn_line_parts = churn_line.split("\t")
                insertions = 1
                insertions_str = churn_line_parts[0]
                if insertions_str != "-":
                    insertions = int(insertions_str)

                deletions = 1
                deletions_str = churn_line_parts[1]
                if deletions_str != "-":
                    deletions = int(deletions_str)
                total_churn = insertions + deletions
                file = churn_line_parts[2]
                result = result + f'{epoch},{tmsp},"{author}",{file},{total_churn}\n'

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
