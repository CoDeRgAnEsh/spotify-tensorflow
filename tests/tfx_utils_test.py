# -*- coding: utf-8 -*-
#
# Copyright 2017-2019 Spotify AB.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from unittest import TestCase

from spotify_tensorflow.tfx.utils import clean_up_pipeline_args


class TFXUtilsTest(TestCase):
    def test_clean_up_pipeline_args(self):
        pipeline_args = [
            "--project=1",
            "--tempLocation=gs://tmp",
            "--jobName",
            "test",
            "--extra=1",
            "--requirements_file=requirements.txt"
        ]
        expected = [
            "--project=1",
            "--temp_location=gs://tmp",
            "--job_name=test",
            "--requirements_file=requirements.txt"
        ]
        self.assertEqual(clean_up_pipeline_args(pipeline_args), expected)
