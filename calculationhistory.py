calculations = []
def add_to_history(calculation):
    calculations.append(calculation)

def show_history():
    if not calculations:
       return "no calculations yet"

    history_text = ""
    for calculation in calculations:
        history_text = "" + calculation + '\n'

        return history_text
    def clear_history():
        calculations.clear()