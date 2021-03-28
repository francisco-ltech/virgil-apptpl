import sys,os
sys.path.append(os.getcwd())

config = {
    "virgil_fs": {"local": "/tmp/my_app", "databricks": "dbfs:/jobs/"}, 
    "file-checkpoint-dir": {"local": "/tmp/my_app/checkpoint-dirs/file", "databricks": "/mnt/raw/_checkpoints/file/"},
    "json-input-data": {"local": "/tmp/my_app/input-data/json", "databricks": "/mnt/raw/file_input_data/"},
    "json-output-data": {"local": "/tmp/my_app/output-data/json", "databricks": "/mnt/raw/file_output_data/"},
    "delta-checkpoint-dir": {"local": "/tmp/my_app/checkpoint-dirs/delta", "databricks": "/mnt/raw/_checkpoints/delta/"},
    "delta-input-data": {"local": "/tmp/my_app/input-data/delta", "databricks": "/mnt/raw/delta_input_data/"},
    "delta-output-data": {"local": "/tmp/my_app/output-data/delta", "databricks": "/mnt/raw/delta_output_data/"},
    "hadoop": os.path.join(os.getcwd(), 'src\jobs\hadoop') 
}

def get_config_setting(spark, config, key):
  """
  
  """
  if spark.sparkContext.appName == 'Databricks Shell':
    return config.get(key).get("databricks")
  else:
    return config.get(key).get("local")

os.environ['HADOOP_HOME'] = config.get("hadoop")

