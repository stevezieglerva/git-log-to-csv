#git log --reverse --all -M -C --numstat --format="^^%h--%ct--%cI--%cn%n" > ~/temp/git_log_react.txt


python3 git_log_to_csv.py sample_input/git_log_govuk.txt > results.csv
python3 git_log_to_csv.py sample_input/git_log_react.txt > results.csv
