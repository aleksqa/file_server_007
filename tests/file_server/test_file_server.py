from src import file_service
from mock import mock_open


def test_list_dir_success(mocker):
    list_dir_mock = mocker.patch('os.listdir')
    list_dir_mock.return_value = ['a', 'b', 'c']

    res = file_service.list_dir()

    list_dir_mock.assert_called_once()
    assert res == ['a', 'b', 'c']


# def test_unique_file_name_duplicate(mocker):
#     random_string_mock = mocker.patch("src.utils.random_string")
#
#     def random_string():
#         if len(random_string_mock.mock_calls) == 1:
#             return "first_filename"
#         return "second_filename"
#
#     random_string_mock.side_effect = random_string
#
#     def path_exist(filename):
#         return filename == "first_filename"
#
#     path_exist_mock = mocker.patch("os.path.exists")
#     path_exist_mock.side_effect = path_exist
#
#     file_service.unique_file_name()
#
#     assert len(random_string_mock.mock_calls) == 2
#     assert len(path_exist_mock.mock_calls) == 2


def test_create_file_success(mocker):
    # AAA Arrange Act Assert - разбить зрительно на три акта
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    mocker.patch("src.utils.random_string").return_value = "test_random_string"

    file_service.create_file("blabla")

    mocked_open.assert_called_with("test_random_string", "w")
    mocked_open().write.assert_called_with("blabla")


def test_change_dir_success_flow(mocker):
    mocker.patch("os.path.isdir").return_value = True
    ch_dir_mocker = mocker.patch("os.chdir")
    file_service.change_dir("anydir")
    # assert file_service.change_dir("anydir") is True
    ch_dir_mocker.assert_called_with("anydir")


def test_change_dir_no_such_directory(mocker):
    mocker.patch("os.path.isdir").return_value = False
    ch_dir_mocker = mocker.patch("os.chdir")
    file_service.change_dir("anydir")
    # assert file_service.change_dir("anydir") is False
    ch_dir_mocker.assert_not_called()


def test_delete_file_success_flow(mocker):
    mocker.patch("os.path.isfile").return_value = True
    delete_mocker = mocker.patch("os.remove")
    file_service.delete_file("anyfile")
    # assert file_service.delete_file("anyfile") is True
    delete_mocker.assert_called_with("anyfile")


def test_delete_file_not_exist(mocker):
    mocker.patch("os.path.isfile").return_value = False
    delete_mocker = mocker.patch("os.remove")
    file_service.delete_file("anyfile")
    # assert file_service.delete_file("anyfile") is False
    delete_mocker.assert_not_called()


def test_read_file_success(mocker):
    mocker.patch("os.path.isfile").return_value = True
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    mocked_open().read.return_value = "blabla"

    assert file_service.read_file("anyfile") == "blabla"
    mocked_open.assert_called_with("anyfile", "r")


def test_read_file_not_exist(mocker):
    mocker.patch("os.path.isfile").return_value = False
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)

    assert file_service.read_file("anyfile") is None
    mocked_open.assert_not_called()