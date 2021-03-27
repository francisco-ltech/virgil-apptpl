from configuration import config, get_config_setting
from validations import validate_presence_of_columns

from pyspark.sql import SparkSession


def run(spark, config):

    df = (spark.readStream
          .format("delta")
          .load(get_config_setting(spark, config, "delta-input-data")))


    # You may want to clean or qualify data before sink ...
    validate_presence_of_columns(df, ["id"])

    query = (df.writeStream
             .format("delta")
             .option("checkpointLocation", get_config_setting(spark, config, "delta-checkpoint-dir"))
             .outputMode("append")
             .trigger(once=True)
             .start(get_config_setting(spark, config, "delta-output-data")))

    query.awaitTermination()

    new_df = (spark.read
          .format("delta")
          .load(get_config_setting(spark, config, "delta-output-data")))

    new_df.printSchema()


if __name__ == "__main__":
    spark = (SparkSession
             .builder
             .appName("Ingest Data")
             .master("local[3]")
             .config("spark.streaming.stopGracefullyOnShutdown", "true")
             .config("spark.sql.streaming.schemaInference", "true")
             .config("spark.jars.packages", "io.delta:delta-core_2.12:0.7.0")
             .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
             .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
             .getOrCreate())

    #print("pass")
    run(spark, config)
