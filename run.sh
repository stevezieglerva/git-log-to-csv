#git log --reverse --all -M -C --numstat --format="^^%ct--%cI--%cn%n" > git_log.txt


python3 git_log_to_csv.py sample_input/git_log_govuk.txt > results.csv
