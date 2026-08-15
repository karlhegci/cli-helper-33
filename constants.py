AUTORUN_INTERVAL = 0.1  # time in seconds between clicks
MAX_CLICKS = 1000  # maximum number of clicks

CLICK_BUTTONS = {  # mapping of button names to their codes
    'left': 1,
    'middle': 2,
    'right': 3,
}

ERROR_MESSAGES = {  # common error messages
    'over_limit': 'Exceeded the maximum number of clicks.',
    'invalid_button': 'The specified button is not valid.',
}

CONFIGURATION = {
    'click_speed': AUTORUN_INTERVAL,
    'max_clicks': MAX_CLICKS,
    'default_button': 'left',
}