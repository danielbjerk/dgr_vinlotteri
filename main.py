import random
import pandas as pd
import numpy as np

random.seed("DGR")

str_path = "siste_transaksjoner.xlsx"    # Relative path
str_name_col = "Forklaring"
str_amount_col = "Inn på konto"
fl_entry_cost = 5.0

df_kontoutskrift = pd.read_excel(str_path)

list_entries = []
fl_payments = 0
for _index, row in df_kontoutskrift.iterrows():
    str_entree_name = row[str_name_col]
    int_entree_ticket_amount = int(row[str_amount_col] // fl_entry_cost)
    fl_payments += float(row[str_amount_col])
    list_entries.extend([str_entree_name] * int_entree_ticket_amount)

print(fl_payments)
print(random.choice(list_entries))
print(random.choice(list_entries))