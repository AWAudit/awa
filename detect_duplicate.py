def detect_duplicates(frame):
    duplicates = frame[frame.duplicated()]
    if not duplicates.empty:
        print("Duplicate records found:")
        print(duplicates)
    else:
        print("No duplicate records found.")
    return duplicates

df = pd.DataFrame(data)
detect_duplicates(df)


