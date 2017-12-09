from geo_game import check_user_guess_correct


def test_check_user_guess_correct():
    assert check_user_guess_correct("Zagreb", "Croatia") == True

    assert check_user_guess_correct("Zagreb", "United Kingdom") == False

    print "All test successfully passed!"


test_check_user_guess_correct()


