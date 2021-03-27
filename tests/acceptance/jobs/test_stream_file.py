import os
import shutil

from configuration import config, get_config_setting
from src.jobs import stream_file


class TestStreamFileJob:

    def test_run(self, spark_session):
        """ Tests stream_file.run function that acts as a Spark job. """

        if os.path.exists(get_config_setting(spark_session, config, "json-output-data")) and os.path.exists(get_config_setting(spark_session, config, "file-checkpoint-dir")):
            shutil.rmtree(get_config_setting(spark_session, config, "json-output-data"))
            shutil.rmtree(get_config_setting(spark_session, config, "file-checkpoint-dir"))

        stream_file.run(spark_session, config)

        assert os.listdir(get_config_setting(spark_session, config, "json-output-data"))
