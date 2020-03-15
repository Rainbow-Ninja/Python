# We've made the balance history readonly for the auto marking.
BALANCE_HISTORY = [107, 201, 201, 225, 216]

def inc_or_dec(days_ago):
  #we need to check how far back we want to go isn't further than the data we have
  if days_ago > len(BALANCE_HISTORY):
    days_ago = len(BALANCE_HISTORY)
  # Avoid -1 because that slice will only have 1 balance!
  for day in range(-days_ago, -1):
    #we want all the array from the day point, not just all but the last number
    days_to_compare = BALANCE_HISTORY[day:]
    balance_difference = days_to_compare[1] - days_to_compare[0]
    if balance_difference > 0:
      print(f'Balance from {abs(day)} days ago INCREASED!')
    elif balance_difference < 0:
      print(f'Balance from {abs(day)} days ago DECREASED!')
    else:
      print(f'Balance from {abs(day)} days ago stayed THE SAME!')
      
d = int(input('How many days of data? '))
inc_or_dec(d)