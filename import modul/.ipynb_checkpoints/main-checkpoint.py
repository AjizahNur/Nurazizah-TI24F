def menu():
    while True:
        print("\nMenu Utama")
        print("1. Aritmatika\n2. Konversi\n3. Ubah Bilangan\n4. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == '1':
            print("\nAritmatika:\n1. Penjumlahan\n2. Perpangkatan\n3. Perkalian")
            sub = input("Pilih: ")
            a = float(input("Angka 1: "))
            b = float(input("Angka 2: "))
            if sub == '1':
                print("Hasil:", penjumlahan(a, b))
            elif sub == '2':
                print("Hasil:", perpangkatan(a, b))
            elif sub == '3':
                print("Hasil:", perkalian(a, b))

        elif pilih == '2':
            print("\nKonversi:\n1. CM ke M\n2. M ke CM")
            sub = input("Pilih: ")
            val = float(input("Nilai: "))
            if sub == '1':
                print("Hasil:", cm_to_m(val))
            elif sub == '2':
                print("Hasil:", m_to_cm(val))
            elif pilih == '3':
            print("\nUbah Bilangan:\n1. Desimal ke Biner\n2. Oktal\n3. Hexa")
            sub = input("Pilih: ")
            val = int(input("Angka desimal: "))
            if sub == '1':
                print("Biner:", desimal_ke_biner(val))
            elif sub == '2':
                print("Oktal:", desimal_ke_oktal(val))
            elif sub == '3':
                print("Hexa:", desimal_ke_heksadesimal(val))

        elif pilih == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan salah!")

menu()


