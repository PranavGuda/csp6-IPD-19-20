####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude unless losing or tied'
strategy_description = 'Always collude unless you are losing or tied, then betray'
    
def move( my_score, their_score):
    '''makes move based on the comparison of my score to their score
    '''
    if my_score <= their_score:
      return 'b'
    else:
      return 'c'
    # This player always colludes.
   
    