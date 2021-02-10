import re
import sys
from datetime import datetime


def main(filename):
    git_log_text = ""
    with open(filename, "r") as file:
        git_log_text = file.read()

    result = process_git_log(git_log_text)
    print(result)


def strip_timezone_offset(timestamp_str):
    timezone_offset_pattern = "[+\-][0-9][0-9]:[0-9][0-9]$"
    return re.sub(timezone_offset_pattern, "", timestamp_str)


def get_churn_int_values_even_if_dash(text_number):
    metric = 1
    if text_number != "-":
        metric = int(text_number)
    return metric


def get_first_directories_from_filename(file):
    file_dir_parts = file.split("/")
    dir_1 = ""
    dir_2 = ""
    if len(file_dir_parts) >= 2:
        dir_1 = file_dir_parts[0]
    if len(file_dir_parts) >= 3:
        dir_2 = file_dir_parts[1]
    return (dir_1, dir_2)


def process_git_log(log):
    commits = log.split("^^")

    result = "epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2\n"
    for number, commit in enumerate(commits):
        if commit != "":
            commit_lines = commit.split("\n")
            commit_basics = commit_lines[0]
            commit_basics_parts = commit_basics.split("--")
            has = commit_basics_parts[0]
            epoch = commit_basics_parts[1]
            tmsp = commit_basics_parts[2]

            # 2019-12-17T09:16:10-05:00
            # yyyy-mm-ddT
            tmsp = strip_timezone_offset(tmsp)
            tmsp_date = datetime.strptime(tmsp, "%Y-%m-%dT%H:%M:%S")
            day_only = tmsp_date.date()
            year = tmsp_date.year
            month = tmsp_date.month
            day = tmsp_date.day

            author = commit_basics_parts[3]

            total_lines = len(commit_lines)
            for row_index in range(3, total_lines - 1):
                churn_line = commit_lines[row_index]
                churn_line_parts = churn_line.split("\t")
                insertions = get_churn_int_values_even_if_dash(churn_line_parts[0])
                deletions = get_churn_int_values_even_if_dash(churn_line_parts[1])
                total_churn = insertions + deletions

                file = churn_line_parts[2]
                dir_1, dir_2 = get_first_directories_from_filename(file)

                result = (
                    result
                    + f'{epoch},{tmsp},{day_only},{year},{month},{day},"{author}",{file},{total_churn},{dir_1},{dir_2}\n'
                )

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
