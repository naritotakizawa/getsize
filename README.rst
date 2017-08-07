=======
getsize
=======

.. image:: https://travis-ci.org/naritotakizawa/getsize.svg?branch=master
    :target: https://travis-ci.org/naritotakizawa/getsize

.. image:: https://coveralls.io/repos/github/naritotakizawa/getsize/badge.svg?branch=master
    :target: https://coveralls.io/github/naritotakizawa/getsize?branch=master


ファイル・ディレクトリのサイズを柔軟に取得するコマンドラインツール

Requirement
===========
:Python: 3.4以上
 
 
Install
=======
::

    pip install -U https://github.com/naritotakizawa/getsize/archive/master.tar.gz


Usage
=====
::

    usage: pysize [-h] [-p PATH] [-s SORT] [-r] [-f] [-u]
    
    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  file or dir path
      -s SORT, --sort SORT  size or name
      -r, --reverse         show reverse
      -f, --full            show full path
      -u, --unit            unit scale

    # カレントディレクトリ内のファイル・ディレクトリのサイズを表示する
    pysize
    
    # target_path内のファイル・ディレクトリを表示する 
    pysize -p target_path
    
    # 10MB のような人に優しい形で表示する
    pysize -p target_path -u
    
    # 相対パスではなくフルパスで表示する
    pysize -p target_path -f
    
    # サイズ順に表示する("size" か "name")
    pysize -s size -u
    
    # 昇順・降順を逆にする
    # pysize -s size -r -u




