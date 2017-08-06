#!/usr/bin/env python3
"""ファイル・ディレクトリのサイズを取得するモジュール."""
import os


SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """Convert a file size to human-readable form.

    http://diveintopython3-ja.rdy.jp/your-first-python-program.html

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    """
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


def get_size(path):
    """pathのサイズを返す.

    基準となるパスを受け取り、中のディレクトリ・ファイルを全て足したサイズを返す

    引数:
        path: 基準となるファイル・ディレクトリのパス

    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):

            # 現在のディレクトリ内の全てのファイルパス
            files_path = [os.path.join(dirpath, file) for file in filenames]
            # それらのサイズを測り、sumで合計を出す
            files_size = sum(
                os.path.getsize(p) for p in files_path if os.path.exists(p)
            )

            # 現在のディレクトリ内の全てのディレクトリパス
            dirs_path = [os.path.join(dirpath, dr) for dr in dirnames]
            # get_size(この関数)にディレクトリのパスを渡していき、改めてサイズを測り、合計を出す
            dirs_size = sum(
                get_size(p) for p in dirs_path if os.path.exists(p)
            )

            return files_size + dirs_size


def _main(path=None, sort_type='size',
          reverse=False, show_full_path=False, unit_scale=False):
    if path is None:
        path = os.curdir

    all_size = []

    if show_full_path:
        path = os.path.abspath(path)

    # カレント以下のファイル・ディレクトリを全て取得し、サイズを測る
    with os.scandir(path) as it:
        for entry in it:
            size = get_size(entry.path)
            all_size.append((entry.path, size))

    # ソート処理
    if sort_type == 'size':
        all_size.sort(key=lambda x: x[1], reverse=reverse)
    elif sort_type == 'name':
        all_size.sort(key=lambda x: x[0], reverse=reverse)

    # 表示処理
    for name, size in all_size:
        if unit_scale:
            size = approximate_size(size)
        print(name, size)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path', help='file or dir path', type=str
    )
    parser.add_argument(
        '-s', '--sort', help='size or name', type=str
    )
    parser.add_argument(
        '-r', '--reverse', help='show reverse', action='store_true'
    )
    parser.add_argument(
        '-f', '--full', help='show full path', action='store_true'
    )
    parser.add_argument(
        '-u', '--unit', help='unit scale', action='store_true'
    )
    args = parser.parse_args()
    _main(args.path, args.sort, args.reverse, args.full, args.unit)


if __name__ == '__main__':
    main()
