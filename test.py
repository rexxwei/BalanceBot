"""
This program is to test the function of each model's functionality.
"""

# import sio as sio
# import display as dis
# import solution as sol

import sio as sio
# import display as dis
import solution as sol

if __name__ == "__main__":
    boa = sio.start_game()

    # test whether IO model works properly & the data is valid
    assert len(boa) == 9            # test raw of matrix	
    for i in range(len(boa)):
        assert len(boa[i]) == 9     # test column of matrix
        for j in range(len(boa[i])):
            assert 0 <= int(boa[i][j]) < 10, "Invalid Figure"  # test value range


    # test whether solution model works properly
    assert sol.test_sol(boa) is True

