def print_models(unprinted_desings, completed_models):

    while unprinted_desings:
        current_design = unprinted_desings.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    print("\nThe Following Models have been printed.")
    for model in completed_models:
        print(model)