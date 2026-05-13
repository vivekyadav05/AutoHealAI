from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

schema = StructType(
    [
        StructField("service", StringType()),
        StructField("cpu", DoubleType()),
        StructField("memory", DoubleType()),
        StructField("latency", DoubleType()),
        StructField("error_rate", DoubleType()),
        StructField("restarts", IntegerType()),
    ]
)


def run():
    spark = SparkSession.builder.appName("autohealai-streaming").getOrCreate()
    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "kafka:9092")
        .option("subscribe", "telemetry")
        .load()
    )
    parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")
    query = parsed.writeStream.format("console").outputMode("append").start()
    query.awaitTermination()


if __name__ == "__main__":
    run()
