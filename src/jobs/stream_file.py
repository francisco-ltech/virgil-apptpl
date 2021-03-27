from configuration import config, get_config_setting
from validations import validate_presence_of_columns

from pyspark.sql import SparkSession


def run(spark, config):

    df = (spark.readStream
          .format("json")
          .load(get_config_setting(spark, config, "json-input-data")))

    # You may want to clean or qualify data before sink ...
    validate_presence_of_columns(df, ["author"])
    
    query = (df.writeStream
             .format("json")
             .option("checkpointLocation", get_config_setting(spark, config, "file-checkpoint-dir"))
             .outputMode("append")
             .trigger(once=True)
             .start(get_config_setting(spark, config, "json-output-data")))

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
