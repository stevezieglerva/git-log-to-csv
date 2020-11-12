import sys
from datetime import datetime


def main(filename):
    git_log_text = ""
    with open(filename, "r") as file:
        git_log_text = file.read()

    result = process_git_log(git_log_text)
    print(result)


def process_git_log(log):
    commits = log.split("^^")

    result = "epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2\n"
    for number, commit in enumerate(commits):
        if commit != "":
            commit_lines = commit.split("\n")
            commit_basics = commit_lines[0]
            commit_basics_parts = commit_basics.split("--")
            epoch = commit_basics_parts[0]
            tmsp = commit_basics_parts[1]
            # 2019-12-17T09:16:10-05:00
            # yyyy-mm-ddT
            tmsp = tmsp.replace("+00:00", "")
            tmsp = tmsp.replace("-04:00", "")
            tmsp = tmsp.replace("-05:00", "")
            tmsp_date = datetime.strptime(tmsp, "%Y-%m-%dT%H:%M:%S")
            day_only = tmsp_date.date()
            year = tmsp_date.year
            month = tmsp_date.month
            day = tmsp_date.day
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
                file_dir_parts = file.split("/")
                dir_1 = ""
                dir_2 = ""
                if len(file_dir_parts) >= 2:
                    dir_1 = file_dir_parts[0]
                if len(file_dir_parts) >= 3:
                    dir_2 = file_dir_parts[1]

                result = (
                    result
                    + f'{epoch},{tmsp},{day_only},{year},{month},{day},"{author}",{file},{total_churn},{dir_1},{dir_2}\n'
                )

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
