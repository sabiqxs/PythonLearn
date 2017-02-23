import os

os.chdir('/Python Projects/CobaSaja/Rename/')
print(os.getcwd())
for n in os.listdir():
    f_name, f_ext = os.path.splitext(n)
    p_month, p_day, p_num = f_name.split('-')

    # menghilangkan Spasi saat parsing, zfill menambahkan 0 di penomoran
    p_month = p_month.strip()
    p_day = p_day.strip()
    p_num = p_num.strip()[1:].zfill(2)

    new_name = '{}-{}-{}{}'.format(p_num, p_month, p_day, f_ext)

    print(new_name)
    # merubah nama file
    os.rename(n, new_name)