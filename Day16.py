# Simple Voting System

candidates = {
    "1": {"name": "John", "votes": 0},
    "2": {"name": "Mary", "votes": 0},
    "3": {"name": "David", "votes": 0}
}

voters = []


def show_candidates():
    print("\nCandidates:")
    for key, candidate in candidates.items():
        print(f"{key}. {candidate['name']}")


def vote():
    voter_name = input("\nEnter your name: ")

    if voter_name in voters:
        print("You have already voted!")
        return

    show_candidates()

    choice = input("Choose candidate number: ")

    if choice in candidates:
        candidates[choice]["votes"] += 1
        voters.append(voter_name)
        print("Vote submitted successfully!")
    else:
        print("Invalid candidate choice!")


def show_results():
    print("\nElection Results")
    print("----------------")

    for candidate in candidates.values():
        print(
            f"{candidate['name']}: {candidate['votes']} votes"
        )


while True:
    print("\n===== Voting System =====")
    print("1. Vote")
    print("2. View Results")
    print("3. Exit")

    option = input("Choose option: ")

    if option == "1":
        vote()

    elif option == "2":
        show_results()

    elif option == "3":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid option!")