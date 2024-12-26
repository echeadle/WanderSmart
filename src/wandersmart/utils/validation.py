# Validation Function
def validate_inputs(name, destination, start_date, end_date):
    if not name:
        return False, "Name is required."
    if not destination:
        return False, "Destination is required."
    if start_date > end_date:
        return False, "Start date must be before the end date."
    return True, None
