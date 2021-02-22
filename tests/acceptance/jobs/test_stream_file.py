import os
import shutil

from src.config import config
from src.jobs import stream_file


class TestFromFileJob:

    def test_run(self, spark_session):
        """ Tests stream_file.run function that acts as a Spark job. """

        if os.path.exists(config.get("json-output-data")) and os.path.exists(config.get("file-checkpoint-dir")):
            shutil.rmtree(config.get("json-output-data"))
            shutil.rmtree(config.get("file-checkpoint-dir"))

        stream_file.run(spark_session, config)

        assert os.listdir(config.get("json-output-data"))
