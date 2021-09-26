import random
import pandas as pd
import numpy as np

random.seed("DGR")

str_path = "kontoutskrift.xlsx"    # Relative path
str_name_col = "Forklaring"
str_amount_col = "Inn på konto"
fl_entry_cost = 5.0

df_kontoutskrift = pd.read_from_excel(str_path)

list_entries = []
for row in df_kontoutskrift:
    str_entree_name = df_kontoutskrift[str_name_col]
    int_entree_ticket_amount = df_kontoutskrift[str_amount_col] // fl_entry_cost
    list_entries.append([str_entree_name] * int_entree_ticket_amount)

random.choice(list_entries)