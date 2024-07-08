def detect_anomalies(frame, column, threshold):
    frame['Z_score'] = (frame[column] - 
                        frame[column].mean()) / frame[column].std()
    anomalies = frame[frame['Z_score'].abs() > threshold]
    if not anomalies.empty:
        print("Anomalies detected:")
        print(anomalies)
    else:
        print("No anomalies detected.")
    return anomalies
