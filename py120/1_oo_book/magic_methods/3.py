"""
Exercise 3
Challenge: Create the classes needed to make the following code work as shown:
Don't worry about ties or whether votes should be singular.
"""
# SECOND EDITION, AFTER VIEWING SOLUTION
class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.votes += other
        return self

class Election:
    def __init__(self,candidates):
        self.candidates = candidates

    def results(self):
        total_votes = 0
        
        highest_votes = 0
        winner = None

        for candidate in self.candidates:
            print(f'{candidate.name}: {candidate.votes} votes')
            total_votes += candidate.votes

            if candidate.votes > highest_votes:
                winner = candidate.name
                highest_votes = candidate.votes
        percent = 100 * highest_votes / total_votes

        print(f'\n{winner} won: {percent}% of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# FIRST EDITION #

# class Election:
#     def __init__(self, candidates):
#         self.candidates_dict = {}
#         for candidate in candidates:
#             self.candidates_dict[candidate.name] = candidate.votes

#     def results(self):
#         for name, votes in self.candidates_dict.items():
#             print(f'{name}: {votes} votes')

#         winner = self.find_winner()
#         percent = self.calc_percent(winner)

#         print(f'\n{winner} won: {percent}% of the votes')

#     def find_winner(self):
#         winner = ""
#         highest = 0
#         for name, votes in self.candidates_dict.items():
#             if votes > highest:
#                 winner = name
#                 highest = votes
#         return winner

#     def calc_percent(self, winner):
#         total = 0
#         for votes in self.candidates_dict.values():
#             total += votes
#         return self.candidates_dict[winner] / total * 100

# class Candidate:
#     def __init__(self, name):
#         self.name = name
#         self.votes = 0

#     def __iadd__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
            
#         self.votes += other


# mike_jones = Candidate('Mike Jones')
# susan_dore = Candidate('Susan Dore')
# kim_waters = Candidate('Kim Waters')

# candidates = {
#     mike_jones,
#     susan_dore,
#     kim_waters,
# }

# votes = [
#     mike_jones,
#     susan_dore,
#     mike_jones,
#     susan_dore,
#     susan_dore,
#     kim_waters,
#     susan_dore,
#     mike_jones,
# ]

# for candidate in votes:
#     candidate += 1

# election = Election(candidates)
# election.results()

# # Mike Jones: 3 votes
# # Susan Dore: 4 votes
# # Kim Waters: 1 votes

# # Susan Dore won: 50.0% of votes