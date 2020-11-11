import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from git_log_to_csv import *


class UnitTests(unittest.TestCase):
    def test_process__given_two_commits_three_files__then_three_lines_created(self):
        # Arrange
        input = """^^1576592170--2019-12-17T09:16:10-05:00--Steve Ziegler


3	5	README.md
0	1	sam-app/add_cw_log_error_metric/CloudFormationReplicator.py
^^1576592605--2019-12-17T09:23:25-05:00--Steve Ziegler


2	1	sam-app/add_cw_log_error_metric/CloudFormationReplicator.py
"""

        # Act
        results = process_git_log(input)
        print(results)

        # Assert
        expected = """epoch,timestamp,author,file,churn_count
1576592170,2019-12-17T09:16:10-05:00,"Steve Ziegler",README.md,8
1576592170,2019-12-17T09:16:10-05:00,"Steve Ziegler",sam-app/add_cw_log_error_metric/CloudFormationReplicator.py,1
1576592605,2019-12-17T09:23:25-05:00,"Steve Ziegler",sam-app/add_cw_log_error_metric/CloudFormationReplicator.py,3
"""
        self.assertEqual(results, expected)

    def test_process__given_insertion_is_dash__then_churn_set_to_two(self):
        # Arrange
        input = """^^1576592170--2019-12-17T09:16:10-05:00--Steve Ziegler


-	-	README.md
"""

        # Act
        results = process_git_log(input)
        print(results)

        # Assert
        expected = """epoch,timestamp,author,file,churn_count
1576592170,2019-12-17T09:16:10-05:00,"Steve Ziegler",README.md,2
"""
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()