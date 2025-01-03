import pytest
from neuro_signal.data_handler import load_data
from neuro_signal.neurofeedback import provide_neurofeedback
from neuro_signal.tracking import track_attention

def test_load_data():
    data = load_data("example_file.txt")
    assert isinstance(data, list)
    assert len(data) > 0

def test_provide_neurofeedback():
    feedback = provide_neurofeedback([1, 2, 3])
    assert isinstance(feedback, str)
    assert "focus" in feedback

def test_track_attention():
    score = track_attention([0.1, 0.5, 0.3])
    assert isinstance(score, int)
    assert 0 <= score <= 100

if __name__ == "__main__":
    pytest.main()