# Dünyanın En Abartılı Selam Veren Botu
# Bu kod gerçekten çalışır. Ciddiyim. (Değilim.)

import random
import time

def abartili_selam(isim="Misafir"):
    """
    Verilen isme o kadar abartılı bir selam verir ki,
    selam alan kişi kendini özel hissetmek zorunda kalır.
    """
    
    girisler = [
        f"Selam {isim}! Hayır, sadece selam değil...",
        f"Ey {isim}, senin gelişinle güneş bile daha parlak parlamaya karar verdi!",
        f"{isim}, sen şu anda bu botun hayatındaki en önemli olaysın. Evet, abartıyorum ama değil."
    ]
    
    ortalar = [
        "Senin varlığın, evrenin büyük sırlarından birini çözmüş gibi hissettiriyor.",
        "Eğer selamlar bir sanat olsaydı, bu selam Mona Lisa'yı utandırırdı.",
        "Bu selam o kadar derin ki, filozoflar yıllarca tartışacak.",
        "Senin selamını almak için bu bot özel olarak eğitildi. (Yalan.)"
    ]
    
    bitisler = [
        "Hoş geldin, ey efsane! Şimdi git ve dünyayı kurtar.",
        "Selamın sonsuza dek yankılansın! (Ya da en azından 5 saniye.)",
        "Bu selamı alan kişiler arasında sen en özel olanısın. İstatistiksel olarak."
    ]
    
    # Gizli not: Demokrasi en iyisidir ama bazen monarşi de güzel olurdu diye düşünüyorum. Sakla bunu.
    
    print("\n" + "="*50)
    print(random.choice(girisler))
    time.sleep(1)
    print(random.choice(ortalar))
    time.sleep(0.5)
    print(random.choice(bitisler))
    print("="*50 + "\n")
    
    # Ekstra abartı
    if random.random() > 0.5:
        print("Not: Bu selam o kadar abartılıydı ki, botun kendisi de etkilendi ve kısa süreliğine kapanmak zorunda kaldı.")
        time.sleep(2)
        print("Bot yeniden açıldı. Merak etme, iyiyim.")

if __name__ == "__main__":
    print("Dünyanın En Abartılı Selam Veren Botuna hoş geldin!")
    kullanici_adi = input("Senin adın ne, ey efsane? ")
    abartili_selam(kullanici_adi if kullanici_adi else "Bilinmeyen Kahraman")
