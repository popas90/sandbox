"""
Usage: python initialize_storage.py user_name directory_path

The script scans the directory_path recursively and finds all files, then
breaks them into chunks, each named by their SHA256 hash.

After that, it will create a directory named user_name which will contain
directories named 00..ff. In each of the directorys, file chunks starting
with that directory's name will be placed. Also, a sqlite database will be
created and stored with these directories, in order to keep track of the file
chunks being stored.
"""
import os
import argparse


def parse_cmd():
    """
    Command-line parser for initialize_storage.
    """
    parser = argparse.ArgumentParser(description="Creates the directory \
             structure and database required for storage.")
    parser.add_argument('user_name', help='string representing the user name')
    parser.add_argument('dir_path', help='path to the directory being \
                        converted')
    return vars(parser.parse_args())


def list_all_files(walk_dir):
    """
    Recursively scans a directory and returns a tuple of lists, the first list
    containing all the file names (with extension) and the second one,
    the relative paths of all the files (relative to the input directory).
    """
    file_names, file_paths = [], []
    for root, subdirs, files in os.walk(walk_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_names.append(filename)
            file_paths.append(filepath)

    return (file_names, file_paths)


def create_hash_dirs(root_dir):
    """
    Inside the root directory, create directories named 00 to ff.
    """
    for i in range(0x10):
        for j in range(0x10):
            os.makedirs(os.path.join(root_dir,
                                     format(i, 'X') + format(j, 'X')))


def split_and_hash_file(file_name, file_path):
    pass


if __name__ == '__main__':
    arguments = parse_cmd()
    print(arguments['user_name'])
    print(arguments['dir_path'])
    file_names, file_paths = list_all_files(arguments['dir_path'])
    print(file_names)
    print(file_paths)
    os.makedirs(arguments['user_name'])
    create_hash_dirs(arguments['user_name'])
