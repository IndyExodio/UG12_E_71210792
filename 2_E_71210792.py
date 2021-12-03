a = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
b = input("Hi Tutu, Silakan Masukkan hari yang ingin Anda telusuri : ")
monday = ("kelas ke-1 Algorima Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK","kelas ke-5 Praktikum INLAN")
tuesday = ("kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia","kelas ke-6 PKN")
thursday = ("kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom")
friday = ("kelas ke-2 Sistem Basis Data","Praktikum Sistem Basis Data","INLAN")

if b == "senin" :
    for i in range(len(monday)):
        print(monday[i])
elif a == "selasa" :
    for i in range(len(tuesday)):
        print(tuesday[i])
elif b == "rabu" :
    print("Hari rabu Anda tidak ada kelas")
elif a == "kamis" :
    for i in range(len(thursday)):
        print(thursday[i])
elif b == "jumat" :
    for i in range(len(friday)):
        print(friday[i])