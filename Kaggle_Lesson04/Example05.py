def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if(name == arrivals[-1]): 
        return False
    number_of_guest = len(arrivals)
    name_index = arrivals.index(name)
    if name_index >= number_of_guest/2:
        return True
    else:
        return False