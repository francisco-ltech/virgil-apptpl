from src.config import config
from src.utilities.dataframe_validations import validate_presence_of_columns

from pyspark.sql import SparkSession


def run(spark, config):

    df = (spark.readStream
          .format("json")
          .load(config.get("json-input-data")))

    # You may want to clean or qualify data before sink ...
    validate_presence_of_columns(df, ["author"])

    query = (df.writeStream
             .format("json")
             .option("checkpointLocation", config.get("file-checkpoint-dir"))
             .outputMode("append")
             .trigger(once=True)
             .start(config.get("json-output-data")))

    query.awaitTermination()


if __name__ == "__main__":
    spark = (SparkSession
             .builder
             .appName("Ingest Data")
             .master("local[3]")
             .config("spark.streaming.stopGracefullyOnShutdown", "true")
             .config("spark.sql.streaming.schemaInference", "true")
             .getOrCreate())

    run(spark, config)
