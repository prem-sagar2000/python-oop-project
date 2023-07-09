def get_user_input(display_text, invalid_message, dtype = str):
    parsed_input = None
    is_valid_input = False
    while not is_valid_input:
        input_ = input(display_text)
        if input_ == '':
            print(invalid_message)
            is_valid_input = False
        else:
            try:
                parsed_input = dtype(input_)
                is_valid_input = True
            except:
                print(invalid_message)

    return parsed_input
    
def is_valid_input(inp=None, min_inp = 1, max_inp = 7):
    return inp and inp in range(min_inp, max_inp) or True

