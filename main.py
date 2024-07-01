from PC import parties
from PC import winning
from State import State_info
from State import states
from State import winning_candidate

print("General Election to Parliamentary Constituencies: Trends & Results June-2024\n")
menu = '''\n
+---------------------------------------------------------------------------------------------------+
|MENU:                                                                                              |
|                                                                                                   |
|PARTY WISE                                                                                         |
|1. Find all the party names                                                                        |                                   
|2. Find total seats won by a party                                                                 |
|3. Find all winning candidates of a party                                                          |
|4. Find all the constituencies won by a party and the candidate who stood in that constituency     |
|5. Find total votes got by the winning candidate of a party                                        |
|                                                                                                   |
|STATE WISE                                                                                         |
|6. Find all the state names                                                                        |
|7. Find total number of constituencies in a state                                                  |
|8. Find all the constituency names in a state                                                      |
|9. Find all winning parties in a state and how many seats they have won                            |
|10. Find all winning candidates name in a state, which constituency they have won and which party  |
|they belong to                                                                                     |
+---------------------------------------------------------------------------------------------------+
ENTER ANY OF THE INDEX NUMBER TO PERFORM ITS FUNCTION (1-10) or enter "q" to stop the program: '''

w = int(input(menu))
while w != 'q':
    if w == 1:
        parties.party_names()
    elif w == 2:
        parties.seats_won()
    elif w == 3:
        winning.candidates_won()
    elif w == 4:
        winning.winning_constitutency()
    elif w == 5:
        winning.votes_won()
    elif w == 6:
        states.snames()
    elif w == 7:
        State_info.total_seats()
    elif w == 8:
        State_info.constituency_name()
    elif w == 9:
        State_info.winning_party()
    elif w == 10:
        winning_candidate.won_candidate()
    else:
        print("wrong input")
    w = int(input(menu))
