import os

config = {
    "virgil_fs": "/tmp/my_app",
    "file-checkpoint-dir": "/tmp/my_app/checkpoint-dirs/file",
    "json-input-data": "/tmp/my_app/input-data/json",
    "json-output-data": "/tmp/my_app/output-data/json",
    "delta-checkpoint-dir": "/tmp/my_app/checkpoint-dirs/delta",
    "delta-input-data": "/tmp/my_app/input-data/delta",
    "delta-output-data": "/tmp/my_app/output-data/delta",
    "hadoop": "c:/tmp/my_app/src/jobs/hadoop/"
}

os.environ['HADOOP_HOME'] = config.get("hadoop")
