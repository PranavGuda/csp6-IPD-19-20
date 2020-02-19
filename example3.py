####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'retaliate but collude'
strategy_description = '''betray the first round and always betray unless they colluded in the previous round'''
    
def move(my_history, their_history):
    '''Make my move based on the history with this player.
    '''
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    elif my_history[-1]=='c' and their_history[-1]=='c':
      return 'c' #colludes only when other person colludes 

    else:
      return'b' # otherwise  betray.