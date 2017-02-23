import os
from datetime import datetime


os.chdir('/Python Projects/CobaSaja')
print(os.getcwd())
# os.chdir('E:\Python Projects\CobaSaja')

# os.mkdir('Belajar-2')
# os.makedirs('Belajars/sub1')

# os.rmdir('Belajars/sub1')
# os.removedirs('Belajar-2/sub1')
# os.rename('Belajars', 'CobaSaja')

# mod_time = os.stat('Demos.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.stat('Demos.txt'))

''' berjalan ke semua direktori yang ada
for dirpath, dirnames, filenames in os.walk('E:\Python Projects\CobaSaja'):
    print('Current path:', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()
'''
# os.environ.get('HOME')
# print(os.environ.get('HOME'))
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)
# print(os.listdir())

# print(os.path.split('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.isdir('/tmp/test.txt'))
# print(os.path.splitext('/tmp/test.txt'))
# print(dir(os.path))