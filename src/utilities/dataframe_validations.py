class DataFrameMissingColumnError(ValueError):
    """raise this when there's a DataFrame column error"""


def validate_presence_of_columns(df, required_col_names):
    all_col_names = df.columns
    missing_col_names = [x for x in required_col_names if x not in all_col_names]
    error_message = "The {missing_col_names} columns are not included in the DataFrame with the following columns {" \
                    "all_col_names}".format(
                        missing_col_names=missing_col_names,
                        all_col_names=all_col_names
                    )
    if missing_col_names:
        raise DataFrameMissingColumnError(error_message)
