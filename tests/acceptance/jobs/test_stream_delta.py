import os
import shutil

from src.config import config
from src.jobs import stream_delta


class TestStreamDeltaJob:

    def test_run(self, spark_session):
        """ Tests stream_file.run function that acts as a Spark job. """

        if os.path.exists(config.get("delta-output-data")) and os.path.exists(config.get("delta-checkpoint-dir")):
            shutil.rmtree(config.get("delta-output-data"))
            shutil.rmtree(config.get("delta-checkpoint-dir"))

        stream_delta.run(spark_session, config)

        assert os.listdir(config.get("delta-output-data"))
