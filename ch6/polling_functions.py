# For Ex 6-6

"""Functions for polling.py."""

def record_votes(invited, poll):
    """
    Ask people to vote for a poll and record their vote. 
    (Print a thank you message if a person already voted.)
    """
    for name in invited:
        if name in poll.keys(): # This person already took the poll.
            print(f"Thank you for responding, {name.title()}!")
        else:                   # Invite this person to take the poll.    
            voted_language = input(f"What's your favourite programming language, "
                                   f"{name.title()}? ")
            poll[name] = voted_language.lower()


def count_votes(votes, poll):
    """Count the votes in the poll."""
    for language in poll.values():
        if language in votes.keys(): # Increment vote for that language.
            votes[language] += 1
        else:                        # Add the language for voting.
            votes[language] = 1


def display_results(votes):
    """Display the poll results."""
    print("\nHere are the poll results:\n")
    for language, vote_count in votes.items():
        print(f"{language.title()}: {vote_count}")
