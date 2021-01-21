# Ex 6-6
from polling_functions import record_votes, count_votes, display_results

poll = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

invited = {'jen', 'al', 'edward', 'francis', 'lily'}

# Take the vote of the invited people.
record_votes(invited, poll)

# Count the poll votes.
votes = {}
count_votes(votes, poll)

# Display the results of the poll.
display_results(votes)