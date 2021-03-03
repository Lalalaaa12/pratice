"""Ask a user for their personal information one question at a time.
 Then check that the information they entered is valid. Finally,
  print a summary of all the information they entered back to them. """

import datetime
#information on name
def valid_name():
    name = input ('Enter your name: \n').strip().title()

    while not all(ord(letter) in range(65,91) or ord(letter) in range(97,123) for letter in name):
        name = input('Please enter a valid name.\n: ').strip().title()
    return name     
guest = valid_name()

#information on date of birth
def valid_date():
    date_month = input ('Enter your month of birth: \n')
    day, month, year =date_month.split(',')

    isValidDate = True

    try:
        datetime.datetime(int(year),int(month),int(day))
        datetime.datetime(int(day), int(month), int(year))
        datetime.datetime(int(year), int(month),int(day))

    except ValueError:


