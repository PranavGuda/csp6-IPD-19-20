####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Betray twice'
strategy_description = 'If they betray once, betray twice'
    
def move(their_history):
    '''Make move based on when they betray
    '''
    # This player betrays twice
    for i in their_history:
      if 'b' == i:
        return 'b'*2
    