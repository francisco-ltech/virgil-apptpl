import os
import shutil

from configuration import config, get_config_setting
from src.jobs import stream_delta


class TestStreamDeltaJob:

    def test_run(self, spark_session):
        """ Tests stream_file.run function that acts as a Spark job. """

        if os.path.exists(get_config_setting(spark_session, config, "delta-output-data")) and os.path.exists(get_config_setting(spark_session, config, "delta-checkpoint-dir")):
            shutil.rmtree(get_config_setting(spark_session, config, "delta-output-data"))
            shutil.rmtree(get_config_setting(spark_session, config, "delta-checkpoint-dir"))

        stream_delta.run(spark_session, config)

        assert os.listdir(get_config_setting(spark_session, config, "delta-output-data"))
