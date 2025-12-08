# from models.tournament import Tournament
# from LL.TournamentLL import TournamentLL

# if __name__ == "__main__":
#     new_tournament = Tournament(
#         name = '',
#         type='',
#         location='',
#         start_date='',
#         end_date='',
#         contact_person=None,
#         events=[],
#     )
#     log_layer = TournamentLL(None)
#     results = log_layer.validate_tournament(new_tournament)
#     assert results == ['Name: Tournament name cannot be empty.', "Type: Tournament type must be 'Knockout' or 'Double Elimination'.", 'Dates: Invalid date format. Use yyyy.mm.dd']

#     new_tournament = Tournament(
#         name = 'Palla Ball',
#         type='Knockout',
#         location='',
#         start_date='454545',
#         end_date='7767',
#         contact_person=None,
#         events=[],
#     )
#     log_layer = TournamentLL(None)
#     results = log_layer.validate_tournament(new_tournament)
#     print(results)
#     assert results == ["Type: Tournament type must be 'Knockout' or 'Double Elimination'.", 'Dates: Invalid date format. Use yyyy.mm.dd']
