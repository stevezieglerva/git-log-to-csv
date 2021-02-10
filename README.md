# git-log-to-csv
This python script reads a pre-generated git log output text file and creates a CSV file of useful columns that can be use for further analysis. There are lots of existing tools that do this but seem to have been abandoned or require server software to present visualizations of the data. This script creates a CSV file that be analyzed or visualized by a separate process. 


## Usage
Create a git log text file with the required format. Navigate to desired local repo and run this command:
```
git log --reverse --all -M -C --numstat --format="^^%h--%ct--%cI--%cn%n" > git_log.txt
```

The output will look like this:
```
^^d7950ef--1584634972--2020-03-19T16:22:52+00:00--Bill Franklin


29	0	.gitignore
1	0	.rspec
1	0	.ruby-version
29	0	Gemfile
299	0	Gemfile.lock
1	0	Procfile
22	0	README.md
11	0	Rakefile
2	0	app/assets/config/manifest.js
...
```



Run the python script passing in the git log text file as a command line argument
```
python3 git_log_to_csv.py git_log.txt > results.csv
```

The results.csv will look like this:
```
commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2
d7950ef,1584634972,2020-03-19T16:22:52,2020-03-19,2020,3,19,"Bill Franklin",.gitignore,29,,
d7950ef,1584634972,2020-03-19T16:22:52,2020-03-19,2020,3,19,"Bill Franklin",.rspec,1,,
...
```

## Tests
```
>. run_tests.sh  

Generating HTML reports... 
reports/test_results.json_test_git_log.UnitTests.html


🗃  Test Results:


📋 test_git_log.UnitTests:
   Status  | Test
   ---------------------------------------------------
   ✅ pass  | test_process__given_file_in_one_dir__then_dir_1_correct                         
   ✅ pass  | test_process__given_insertion_is_dash__then_churn_set_to_two                    
   ✅ pass  | test_process__given_timezone_is_gmt__then_results_are_correct                   
   ✅ pass  | test_process__given_two_commits_three_files__then_three_lines_created           

🗂  Total Tests: 4

👍🎉 All tests passed!
Name                Stmts   Miss  Cover
---------------------------------------
git_log_to_csv.py      58      7    88%
88%
🏆 Coverage is good
```
