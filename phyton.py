# 




# NEW TASK

# İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.
# İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  istifadə edəcəyik.   
# Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.      

class Hesab:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balans_artir(self, miktar):
        self.balans += miktar
        print("Balansınız artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, miktar):
        if miktar > self.balans:
            print("Balansınız kifayət qədər deyil.")
        else:
            self.balans -= miktar
            print("Balansınızdan", miktar, "məbləğində pul çıxarıldı. Yeni balans:", self.balans)

    def balans_goster(self):
        print("Hesab nömrəsi:", self.hesab_nomresi)
        print("Balans:", self.balans)


class Kredit(Hesab):
    def __init__(self, hesab_nomresi, balans, kredit_miqdari):
        super().__init__(hesab_nomresi, balans)
        self.kredit_miqdari = kredit_miqdari

    def kredit_ver(self, miktar):
        self.balans += miktar
        self.kredit_miqdari += miktar
        print("Kreditinizə", miktar, "məbləğində pul əlavə olundu. Yeni kredit miqdarı:", self.kredit_miqdari)

    def kredit_odenisi(self, miktar):
        if miktar > self.balans:
            print("Balansınız kifayət qədər deyil.")
        else:
            self.balans -= miktar
            self.kredit_miqdari -= miktar
            print("Kreditinizdən", miktar, "məbləğində pul ödənilmişdir. Yeni kredit miqdarı:", self.kredit_miqdari)
            print("Balansınız:", self.balans)


hesab1 = Kredit(123456, 1000, 500)
hesab1.balans_artir(200)
hesab1.pul_cixar(300)
hesab1.balans_goster()
hesab1.kredit_ver(200)
hesab1.kredit_odenisi(100)
hesab1.balans_goster()
