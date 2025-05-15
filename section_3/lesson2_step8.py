def test_input_text(expected_result, actual_result):
    t1 = expected_result
    t2 = actual_result
    assert expected_result == actual_result, f"expected {t1}, got {t2}"


test_input_text(1, 6)
