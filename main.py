
#listedeki elemanı sil(pop)#
alisveris_listesi=["su","ekmek","domates","cukulata"]
alisveris_listesi.pop(3)
print(alisveris_listesi)
#listedeki tüm elemanları sil(clear)#
alisveris_listesi=["su","ekmek","domates","cukulata"]
alisveris_listesi.clear()
print(alisveris_listesi)
#bir elemanın konumunu bul(ındex)#
alisveris_listesi=["su","ekmek","domates","cukulata"]
print(alisveris_listesi.index("ekmek"))
#listeleri birleştir(extend)#
alisveris_listesi=["su","ekmek","domates","cukulata"]
ders_listesi=["türkçe","matematik","kimya","fizik"]
alisveris_listesi.extend(ders_listesi)
print(alisveris_listesi)
#listedeki elemanı sil(remove#)
alisveris_listesi=["su","ekmek","domates","cukulata"]
alisveris_listesi.remove("domates")
print(alisveris_listesi)  