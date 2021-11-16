import pandas as pd
def lambda_handler(event,context):    
    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst)
    print(df)
    print("Successful Done x1")