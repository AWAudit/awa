def column_consistency_check(reference_frame, target_frame):
    
    # Find columns in reference_frame that are missing in target_frame
    missing_in_target = [column for 
                         column in reference_frame.columns 
                         if column not in target_frame.columns]
    
    # Find columns in target_frame that are missing in reference_frame
    missing_in_reference = [column for 
                            column in target_frame.columns 
                            if column not in reference_frame.columns]
    
    # Report missing columns
    if missing_in_target:
        print(f'missing in target: {missing_in_target}')
    if missing_in_reference:
        print(f'missing in reference: {missing_in_reference}')
    
    # Convert common columns to float in the target_frame
    common_columns = [column for 
                      column in reference_frame.columns 
                      if column in target_frame.columns]
    for column in common_columns:
        target_frame[column] = target_frame[column].astype(float)
    
    return target_frame
