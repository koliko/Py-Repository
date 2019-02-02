#===============================================================#
# this is the database to hold all the words the bot will use to#
# communicate with the user. Everythig will be saved to a test  #
# file.                                                         #
#===============================================================#

rules = {'if (.*)':
             ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}',
              'Really--if {0}'],
         'I want (.*)':
             ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'do you think (.*)':
             ['if {0}? Absolutely.', 'No chance'],
         'do you remember (.*)':
             ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'],
         'thank (.*)':
             ['thank you {0}', 'you are welcome {0}']
         }


part_of_speech = {
                  'noun':
                        ['my','you','your'],

                  'pronoun':
                          ['your','me','my']
}