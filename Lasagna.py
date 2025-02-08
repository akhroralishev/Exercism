EXPECTED_BAKE_TIME = 40  
PREPARATION_TIME = 2  

def bake_time_remaining(elapsed_bake_time):
    """Qolgan pishish vaqtini hisoblaydi."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time  

def preparation_time_in_minutes(layers):
    """Qatlamlar soniga qarab tayyorlanish vaqtini hisoblaydi."""
    return layers * PREPARATION_TIME  

def elapsed_time_in_minutes(layers, bake_time):
    """Jami sarflangan vaqtni hisoblaydi."""
    prep_time = preparation_time_in_minutes(layers)
    return prep_time + bake_time
