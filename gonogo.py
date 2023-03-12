import pandas as pd

# Load metrics data from a CSV file
df = pd.read_csv('metrics.csv')

# Calculate total bugs, features, lines of code, and test coverage across all milestones
all_bugs = df['Bugs'].sum()
all_features = df['Features'].sum()
all_loc = df['Lines of Code'].sum()
all_coverage = df['Test Coverage'].mean()
# Set predetermined decision criteria
min_bugs = 10
min_features = 5
max_loc = 10000
min_coverage = 0.8

# Define a function to evaluate the decision criteria
def eval_criteria(all_bugs, all_features, all_loc, all_coverage, min_bugs, min_features, max_loc, min_coverage):
    # Check total bugs
    if all_bugs < min_bugs:
        return 'no-go', 'Enough bugs have not been found.'
    # Check total features
    if all_features < min_features:
        return 'no-go', 'Features have not been developed properly.'
    # Check total lines of code
    if all_loc > max_loc:
        return 'no-go', 'Code has been written in excess.'
    # Check test coverage
    if all_coverage < min_coverage:
        return 'no-go', 'Test coverage is too low.'
    # If all criteria are met, return a go decision
    return 'go', 'Project meets the criteria.'

# Call the eval_criteria function with the calculated metrics and decision criteria
decision, reason = eval_criteria(all_bugs, all_features, all_loc, all_coverage, min_bugs, min_features, max_loc, min_coverage)

# Print the decision and reason
print('Decision: {}\nReason: {}'.format(decision, reason))
