import pytest
args_str = "-k test_myfavorite"
args = args_str.split(" ")
pytest.main(args)
