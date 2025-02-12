#########################################################
# Rosenberg Self Esteem Scale
# February 2, 2025
# Colby Wilson
# CSE 111
#########################################################

def get_response(statement, is_positive):
    """Ask the user for their response and return the corresponding score."""
    while True:
        response = input(statement + " (D/d/a/A): ").strip()
        if response in ['D', 'd', 'a', 'A']:
            break
        print("Invalid input. Please enter D, d, a, or A.")
    
    scores = {'D': 0, 'd': 1, 'a': 2, 'A': 3} if is_positive else {'D': 3, 'd': 2, 'a': 1, 'A': 0}
    return scores[response]

def main():
    """Runs the Rosenberg Self-Esteem Scale assessment."""
    print("""
    Welcome to the Rosenberg Self-Esteem Scale.
    Please respond to the following statements with:
    D - Strongly Disagree, d - Disagree, a - Agree, A - Strongly Agree.
    """)
    
    statements = [
        ("I feel that I am a person of worth, at least on an equal plane with others.", True),
        ("I feel that I have a number of good qualities.", True),
        ("All in all, I am inclined to feel that I am a failure.", False),
        ("I am able to do things as well as most other people.", True),
        ("I feel I do not have much to be proud of.", False),
        ("I take a positive attitude toward myself.", True),
        ("On the whole, I am satisfied with myself.", True),
        ("I wish I could have more respect for myself.", False),
        ("I certainly feel useless at times.", False),
        ("At times I think I am no good at all.", False)
    ]
    
    total_score = sum(get_response(statement, is_positive) for statement, is_positive in statements)
    
    print(f"\nYour total self-esteem score is: {total_score}")
    if total_score < 15:
        print("You may have a problematic low self-esteem.")
    else:
        print("Your self-esteem level appears to be in a healthy range.")

main()
