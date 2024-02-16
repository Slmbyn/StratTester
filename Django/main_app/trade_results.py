def short_trade_result (entry_price, exit_price_candidate, volume):
    result_details = {
        'PL_percent': round(((entry_price - exit_price_candidate) / entry_price), 4),
        'PL_abs': round( exit_price_candidate - entry_price, 2),
        'volume': volume,
        'entry_price': entry_price,
        'exit_price': exit_price_candidate,
    }
    return result_details

def long_trade_result(entry_price, exit_price_candidate, volume):
    result_details = {
        'PL_percent': (round(((exit_price_candidate - entry_price) / entry_price),4)),
        'PL_abs': round( exit_price_candidate - entry_price, 2),
        'volume': volume,
        'entry_price': entry_price,
        'exit_price': exit_price_candidate,
    }
    return result_details

def long_trade(api_data, current_index, entry_price, volume):
    # loop thru stock data until exit criteria is met
    for exit_point in api_data['results'][current_index:]:
        # check each 5min candle's closing price until it meets exit criteria
        exit_price_candidate = exit_point['c']              #'C'
        # Winning trade
        if exit_price_candidate >= (entry_price + 1): #Takes profit when price is $1 above entry price
            result_details = long_trade_result(entry_price, exit_price_candidate, volume)
            return result_details
        # Losing trade
        elif exit_price_candidate <= (entry_price - 0.50): #Takes loss when price is $0.50 below entry price
            result_details = long_trade_result(entry_price, exit_price_candidate, volume)
            return result_details
        # No exit criterea met
        else:
            result_details = {
                'PL_percent': 0.00,
                'PL_abs': 0.00,
                'volume': volume,
                'entry_price': entry_price,
                'exit_price': entry_price,
            }
            return result_details

def short_trade(api_data, current_index, entry_price, volume):
    print(f'API Data in short_trade: {api_data}')
    print(f'current_index in short_trade: {current_index}')
    print(f'entry_price in short_trade: {entry_price}')
    print(f'volume in short_trade: {volume}')
    # loop thru stock data until exit criteria is met
    for exit_point in api_data['results'][current_index:]:
        print(f'Exit_Point is: {exit_point}')
        # check each 5min candle's closing price until it meets exit criteria
        exit_price_candidate = exit_point['c']
        # profitable exit criterea
        if exit_price_candidate <= (entry_price - 1): #Takes profit when price is $1 below entry price
            result_details = short_trade_result(entry_price, exit_price_candidate, volume)
            return result_details
        elif exit_price_candidate >= (entry_price - 0.50): #Takes loss when price is $0.50 above entry price
            result_details = short_trade_result(entry_price, exit_price_candidate, volume)
            return result_details
        else:
            result_details = {
                'PL_percent': 0.00,
                'PL_abs': 0.00,
                'volume': volume,
                'entry_price': entry_price,
                'exit_price': entry_price,
            }
            return result_details
