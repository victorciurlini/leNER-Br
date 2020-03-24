''' Test module used to automatize tests for the leNER-BR model adaptation
    to AILAB pipeline
    Note: this file should be executed from the directory above this test
    folder
'''
import pytest
from tests_helper import IO_FOLDER_RELATIVE_PATH, load_expected_io
from ailabner import entity_treatment


@pytest.mark.parametrize(
    'load_expected_io', [('input_1.txt', 'output_1.txt')], indirect=True)
def test_replace_entity_tokens(load_expected_io):
    input_document, expected_output = load_expected_io
    predicted_output = entity_treatment(input_document)
    assert predicted_output == expected_output