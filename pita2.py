def susun_bilangan():
    bilangan = [22, 44, 77, 33, 55, 99, 66, 11, 44]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)