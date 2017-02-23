#file objects

import os

os.chdir('/Python Projects/CobaSaja')
print(os.getcwd())
# print(os.listdir())

# membaca file 'r' write 'w' appending 'a' read n write 'r+'

 # f = open('Demos.txt', 'r')
# print(f.name)
# print(f.mode)



# with open('Demos.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readline()
    # f_contents = f.readlines()
    # print(f_contents)
    # print(f_contents, end='')
    #
    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:
    #     print(line, end='')

    # f_contents = f.read(20)
    # print(f_contents, end='')

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # # while len(f_contents) > 0:
    # #     print(f_contents, end='*')
    # #     f_contents = f.read(size_to_read)
    #
    # f.seek(0)
    # f_contents = f.read(size_to_read)
    # print(f_contents)

# dengan TXT
with open('Demos.txt', 'r') as g:
    # g.write('Test')
    # g.seek(0)
    # g.write('R')

    # print(f.tell())
    # mengcopy semua isi dari Demos.tx
    with open('Demos_copy.txt', 'w') as wf:
        for line in g:
            wf.write(line)


#dengan file IMAGE
with open('oops.PNG', 'rb') as rf:
    with open('oops_copy.PNG', 'wb') as wfs:
        # for lines in rf:
        #     wfs.write(lines)
        oops_size = 4096
        rf_oops = rf.read(oops_size)
        while len(rf_oops) > 0:
            wfs.write(rf_oops)
            rf_oops = rf.read(oops_size)
    # print(f.closed)

# f.close()