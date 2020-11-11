def main():
    process_git_log("")


def process_git_log(log):
    commits = log.split("^^")

    # replace -- with commas
    commits_commas = [c.replace("--", ",") for c in commits]
    commits_commas = [c for c in commits_commas if c != ""]

    result = ""
    for commit in commits_commas:
        commit_lines = commit.split("\n")
        commit_basics = commit_lines[0]
        total_lines = len(commit_lines)
        for row_index in range(3, total_lines - 1):
            print(row_index)
            churn_line = commit_lines[row_index]
            churn_line_parts = churn_line.split("\t")
            insertions = int(churn_line_parts[0])
            deletions = int(churn_line_parts[1])
            total_churn = insertions + deletions
            file = churn_line_parts[2]
            result = result + f"{commit_basics},{file},{total_churn}\n"

    return result


if __name__ == "__main__":
    main()
