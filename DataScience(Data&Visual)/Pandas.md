### df add data

#### append

    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    # create a new row to append
    new_row = pd.DataFrame({'A': [5], 'B': [6]})
    df = df.append(new_row, ignore_index=True)

#### .loc[]

    df.loc[len(df)] = [5, 6]

#### .join()
#### .concat()

    df1 df2
    # concatenate the two DataFrames using .concat()
    df = pd.concat([df1, df2], ignore_index=True)

#### Merge

    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'key': ['K0', 'K1']})
    df2 = pd.DataFrame({'C': [5], 'D': [6], 'key': ['K1']})

    # merge the two DataFrames using .merge()
    df = pd.merge(df1, df2, on='key', how='outer')
