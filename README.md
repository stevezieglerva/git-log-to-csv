# git-log-to-csv
This python script reads a pre-generated git log output text file and creates a CSV file of useful columns that can be use for further analysis. There are lots of existing tools that do this but seem to have been abandoned or require server software to present visualizations of the data. This script creates a CSV file that be analyzed or visualized by a separate process. 

It was inspired by Adam Tornhill's [GOTO 2019 Prioritizing Technical Debt as if Time and Money Matters](https://www.youtube.com/watch?v=fl4aZ2KXBsQ) talk.


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
commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
d7950ef,1584634972,2020-03-19T16:22:52,2020-03-19,2020,3,19,"Bill Franklin",.gitignore,29,,,,
d7950ef,1584634972,2020-03-19T16:22:52,2020-03-19,2020,3,19,"Bill Franklin",.rspec,1,,,,
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

## Samples

### GovUK Coronavirus From   
I analyzed the GovUK [govuk-coronavirus-vulnerable-people-form](https://github.com/jpluscplusm/govuk-coronavirus-vulnerable-people-form) repo since I had [written](https://www.linkedin.com/pulse/how-govuk-used-engineering-ux-help-extremely-steve-ziegler/) about it. Here are the raw text and csv files along with the Excel pivot tables used to create some visualizations.

* [git_log_govuk.txt](samples/git_log_govuk.txt) raw git log  
* [govuk.csv](samples/govuk.csv) resulting csv file
* [govuk.xlsx](samples/govuk.xlsx) Excel with pivot tables and charts

Authors
![](samples/govuk_author.png)

Dirs
![](samples/govuk_dirs.png)

Date
![](samples/govuk_date.png)

### React 
I also analyzed the React git log. For file size considerations, I've only included the raw [git log](samples/git_log_react.txt).

Authors
![](samples/react_author.png)

Dirs
![](samples/react_dir_1.png)

Date
I like how you can see when they put a lot of effort into documentation.
![](samples/react_date.png)



