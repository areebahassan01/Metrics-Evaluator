## MetricsEvaluation
This script loads metrics data from a CSV file into a pandas DataFrame and calculates the total bugs, features, lines of code, and test coverage across all milestones. It then evaluates these metrics based on predetermined decision criteria for minimum bugs, minimum features, maximum lines of code, and minimum test coverage.
## Requirements
Python 3.6 or higher
pandas library
## Installation
Download the script files.
Install the required libraries using pip: pip install pandas
## Usage
Place the metrics data CSV file in the same directory as the script files.
Open the gonogo.py file and customize the decision criteria as needed.
Run the script: python gonogo.py
The script will output a "go" or "no-go" decision and a reason based on the calculated metrics and decision criteria.
## Customization
You can customize the decision criteria by modifying the following variables in the metrics_evaluation.py file:
MIN_BUGS: minimum number of bugs required for a "go" decision
MIN_FEATURES: minimum number of features required for a "go" decision
MAX_LOC: maximum number of lines of code allowed for a "go" decision
MIN_COVERAGE: minimum test coverage required for a "go" decision
You can also modify the code in the eval_criteria function to add additional or different decision criteria.
