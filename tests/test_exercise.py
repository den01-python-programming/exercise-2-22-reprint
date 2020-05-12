import pytest
import src.exercise

def test_exercise():
    input_values = ["4"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2],output[3],output[4]] == ["How many times?",\
                                                                            "In a hole in the ground there lived a method",\
                                                                            "In a hole in the ground there lived a method",\
                                                                            "In a hole in the ground there lived a method",\
                                                                            "In a hole in the ground there lived a method"]
