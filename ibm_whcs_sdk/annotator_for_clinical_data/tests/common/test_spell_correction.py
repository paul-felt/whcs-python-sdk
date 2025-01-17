# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ibm_whcs_sdk.annotator_for_clinical_data.tests.common import test_suggestion as ts

class TestSpellCorrectionAnnotation(object):

    @staticmethod
    def test_spelling_correction(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.begin >= 0
                assert annotation.end > annotation.begin
                assert annotation.covered_text is not None
                for suggestion in annotation.suggestions:
                    ts.TestSuggestion.test_spelling_suggestion(suggestion)
