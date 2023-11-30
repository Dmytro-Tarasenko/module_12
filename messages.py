helpmsg = {
    'add': ('add <contact_name> [<phone_numbers>,'
            + '<birthday>]\n'
            + 'Adds  contact with name <contact_name>,'
            + 'phone number <phone_number>  to contact base.\n'
            + '\t<contact_name> contains only one word;\n'
            + '\t<phone_number> - only digits,'
            + ' phones from 6 to 12 digits are acceptable;\n'
            + '\t<birthday> should be in format yyyy-mm-dd or dd-mm-yyyy'
            + 'common separator are allowed [.,/\\].\n'
            + 'If no <contact_name> is provided'
            + ' all data goes to current record\n====='),
    'exit': 'exit\n Prints farewell message, saves data and exits\n=====',
    'show': ('show [lim:N, <ind>, <ind_start>-<ind_end>]\n'
             + 'Shows recorded contacts in addressbook.\n'
             + '\tlim:N - set the limitation of N records to display'
             + ' at once.\nPress "Enter" to proceed "C"  to abort.\n'
             + '\t<ind> - index of record in addressbook to display.\n'
             + '\tMultiple <ind> can be processed.\n'
             + '\t<ind_start>-<ind_end> - display records'
             + ' from <ind_start> to <ind_end>.\n'
             + '\tIt`s possible to combine lim:N and'
             + ' <ind_start>-<ind_end>(only 1 range)\n====='),
    'hello': 'hello\n Shows greeting message.\n=====',
    'change': ('change [<old_name>] <new_name> [<old_phone> <new_phone>]'
               + '[<new_birthday>]\n'
               + 'Changes data of record <old_name> to provided new ones.\n'
               + '\t<old_name> - is the name for record which data needs to'
               + ' be changed. If not specified\ncurrent record is used.\n'
               + '\t<old_phone> <new_phone> - pairs of numbers to change.\n'
               + '\t\tIt`s possible to omit <old_phone> if there is only'
               + ' one number in record.\n'
               + '\t<new_birthday> - new date of birthday.\n====='),
    'help': ('help [<command>]\n'
             + 'Displays help info for <command>\n'
             + '\tList of available commands: hello, add,'
             + ' change, phone, show, exit, help, find.\n====='),
    'del': ('del [<name(s)> | <phone(s)> | <birthday>]\n'
            + 'Removes record(s) with <name(s)> or respective fields for'
            + ' record <name>\n'
            + 'If no <name> is specified current record is used. So "del"'
            + ' with no arguments deletes current record\n'
            + 'If multiple <name(s)> are specified no other fields'
            + ' are allowed\n=====')
}

errormsg = {
    'no_contact_number': ('Provide valid contact name\\'
                          + 'phone number to proceed\n'),
    'future_date': ('Future is not come yet.'
                    + ' Try another date\n'),
    'no_contact': 'Provide contact name to proceed\n',
    'no_number': 'Provide phone number to proceed\n',
    'wrong_number': 'Provided phone number is not valid\n',
    'wrong_contact': 'Provided contact name is not valid\n',
    'contact_or_phone_mis': ('Both contact name and phone number'
                             + ' are needed to proceed\n'),
    'empty_list': ('Nothing to show -'
                   + ' contacts base got no records.\n'
                   + 'Try to fill it first.'),
    'mentor_detected': ('Really!? Doing stuff with no records!?\n'
                        + 'Ulyana, are you here?\n'
                        + 'If yes, THANKS ALOT!\n'),
    'contact_exists': ('Contact`ve been already recorded.'
                       + ' Try another name.\n'),
    'phone_exists': ('Phone`ve been already recorded.'
                     + ' Try another one.\n'),
    'phone_not_found': 'Given phone is not found in record.\n',
    'contact_!exists': 'Contact does not exist. Try another name.\n',
    'params_absense': 'No needed parameter(s) was(were) provided.\n',
    'not_enough_phones': 'Unable to determine phone to change.\n',
    'bad_search_cond': 'Bad search condition were provided.\n',
    'uncertain_show': 'Unable to determine condition for <show>.\n',
    'index_error': 'Given indexes are invalid.]n',
    'change_to_existing': ('Unable to change name'
                           + ' to name of existing contact.\n'),
    'twice_born': 'Humans got only 1 birthday.\n',
    'bday_not_found': 'Given birthday does not match with recorded one.\n',
    'uncertain_del': 'Uncertain entities for removal.\n',
    'empty_exec': 'Executioner needs victims. Something really gone wrong.\n'
}
