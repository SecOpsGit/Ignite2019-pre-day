ct = pd.crosstab(df_errors['machineID'], df_errors['errorID'], rownames=['device'], colnames=['error'], normalize='columns')