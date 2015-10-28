import os
import nose
import shutil
from initialize_storage import list_all_files
from initialize_storage import create_hash_dirs


def setup():
    """
    Creates directory "dir" containing file "file".
    """
    test_dir = os.path.join(os.getcwd(), 'dir')
    os.makedirs(test_dir)
    with open(os.path.join(test_dir, 'file'), 'a') as file_in_dir:
        file_in_dir.write('Write this test string in the file.')


def teardown():
    shutil.rmtree(os.path.join(os.getcwd(), 'dir'))


def test_list_all_files():
    nose.tools.eq_(list_all_files(os.path.join(os.getcwd(), 'dir')),
                   (['file'], [os.path.join(os.getcwd(), 'dir/file')]))


def test_create_hash_dirs():
    path = os.path.join(os.getcwd(), 'dir')
    create_hash_dirs(path)
    cnt = 0
    for root, dirs, files in os.walk(path):
        cnt += len(dirs)
    nose.tools.eq_(cnt, 256)


def test_split_and_hash_file():
    pass
