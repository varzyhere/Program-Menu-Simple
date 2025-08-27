menu = ['Indomie', 'Kopi', 'Es Teh']
price = [6000, 4000, 3000]

print('-----List menu:-----\n')

for i in range(len(menu)):
    print(f'{menu[i]}, harga (Rp{price[i]})')

pesan = input('Apakah anda akan memesan? (Y/N) : ')

if pesan == 'Y' or 'y':
    print('\n-----Silahkan ketik jumlah makanan yang ingin anda pesan (ANGKA)-----')
    for i in range(len(menu)):
        print(f'\n{menu[i]} (Rp{price[i]}) = ')
        if i == 0:
            a = int(input('Berapa jumlah yang ingin anda pesan? : '))
        elif i == 1:
            b = int(input('Berapa jumlah yang ingin anda pesan? : '))
        else:
            c = int(input('Berapa jumlah yang ingin anda pesan? : '))

    print(f'\n-----Catatan Pemesanan-----\n')
    for i in range(len(menu)):
        if i == 0:
            print(f'Anda memesan {menu[i]} sejumlah {a}')
        elif i == 1:
            print(f'Anda memesan {menu[i]} sejumlah {b}')
        else:
            print(f'Anda memesan {menu[i]} sejumlah {c}')

    totalHarga = (a*price[0]) + (b*price[1]) + (c*price[2])
    print(f'\nTotal pesanan anda berjumlah {a + b + c}')
    print(f'Total Harga pesanan anda senilai {totalHarga} rupiah')

    print('\n-----Proses Pembayaran-----')
    hargaBayar = int(input('\nMasukkan uang nominal anda : '))
    while hargaBayar < totalHarga:
        print('Maaf uang anda tidak mencukupi :(')
        hargaBayar = int(input('\nMasukkan uang nominal anda : '))
    else:
        print(f'Uang kembalian anda: {hargaBayar - totalHarga}')
        print('\nTerima kasih telah berkunjung! :)')

else:
    print('\nSuwun telah berkunjung! :)')