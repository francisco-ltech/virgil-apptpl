import pytest
from validations import *
from configuration import *


class TestDataFrameValidations:
    """
    Tests utility functions in dataframe_validations.py
    """

    def test_validate_presence_of_columns_when_column_is_missing(self, spark_session):
        data = [("jose", 1), ("li", 2), ("luisa", 3)]
        source_df = spark_session.createDataFrame(data, ["name", "age"])
        with pytest.raises(DataFrameMissingColumnError) as excinfo:
            validate_presence_of_columns(source_df, ["name", "age", "fun"])
        assert excinfo.value.args[0] == "The ['fun'] columns are not included in the DataFrame with the following " \
                                        "columns ['name', 'age']"

    def test_validate_presence_of_columns_when_all_columns_are_present(self, spark_session):
        data = [("jose", 1), ("li", 2), ("luisa", 3)]
        source_df = spark_session.createDataFrame(data, ["name", "age"])
        validate_presence_of_columns(source_df, ["name"])
