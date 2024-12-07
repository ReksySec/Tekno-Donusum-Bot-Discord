import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı!')


@bot.command(name="geri_donusum")
async def geri_donusum(ctx, cihaz: str):
    geri_donusum_verileri = {
        "laptop": [
            "Laptobunuzun pilini güvenli bir şekilde çıkarın ve yerel geri dönüşüm merkezine bırakın.",
            "Parçalarını satarak gelir elde edebilirsiniz.",
            "Çalışıyorsa çocukların eğitimine destek için bağış yapabilirsiniz.",
            "Eski laptobunuzu atmayın, medya sunucusuna dönüştürün."
        ],
        "telefon": [
            "Telefonunuzu sıfırlayıp bağış yapabilirsiniz.",
            "Bataryasını geri dönüşüm kutusuna atarak doğaya zarar vermeden imha edin.",
            "Telefonunuzu güvenlik kamerasına dönüştürün.",
            "Müzik çalar olarak kullanabilirsiniz."
        ],
        "tablet": [
            "Tabletlerinizi mutfak tarif ekranı olarak değerlendirin.",
            "Çalışıyorsa çocukların online eğitimleri için bağış yapın.",
            "Eski tabletinizi dijital çerçeveye dönüştürün.",
            "Oyun emülatörü olarak yapılandırın."
        ],
        "bilgisayar": [
            "Eski bilgisayarınızı medya sunucusuna dönüştürün.",
            "Parçalarını satıp yenileme projelerinde değerlendirin.",
            "Eski bilgisayarınızı yerel eğitim kurumlarına bağış yapabilirsiniz.",
            "Yedek parça olarak satabilirsiniz."
        ],
        "monitör": [
            "Monitörünüz sağlam ise ikinci el pazarlarında satabilirsiniz.",
            "Monitörünüzü güvenlik kamerası ekranı olarak kullanabilirsiniz.",
            "Fotoğraf veya sanat projeleri için çerçeveye dönüştürün.",
            "Çalışmıyorsa geri dönüşüm merkezine bırakın."
        ],
        "kamera": [
            "Güvenlik sistemi veya canlı yayın cihazı olarak yapılandırabilirsiniz.",
            "Fotoğrafçılık kurslarına bağış yapabilirsiniz.",
            "Akıllı ev projelerine dahil edebilirsiniz.",
            "Doğa kamerası olarak kullanabilirsiniz."
        ],
        "televizyon": [
            "Yerel geri dönüşüm merkezine bırakın.",
            "Parçalarını yaratıcı projelerde kullanabilirsiniz.",
            "Eski oyun konsolları için ekran olarak değerlendirin.",
            "Dijital tabela ekranı olarak yapılandırabilirsiniz."
        ],
        "hoparlör": [
            "Eski hoparlörlerinizi ev sinema sistemine dönüştürün.",
            "Bluetooth hoparlöre dönüştürmek için kitler satın alın.",
            "Ses sistemleri için yedek parça olarak değerlendirin.",
            "Sanat projelerinde kullanın."
        ],
        "oyun_konsolu": [
            "Retro oyun koleksiyonu olarak saklayın.",
            "Eski oyun konsolunuzu yenileyip hobi projelerine ekleyin.",
            "Emülatör kurup retro oyun merkezi yapın.",
            "Oyun konsolunu bilgisayara bağlayarak medya cihazı olarak kullanın."
        ],
        "yazıcı": [
            "Eski yazıcılarınızı parçalayıp geri dönüşüm kutusuna atın.",
            "Yedek parça olarak kullanabilirsiniz.",
            "Yazıcı motorlarını robot projelerinde değerlendirin.",
            "Mühendislik deneylerinde test cihazı olarak kullanın."
        ],
        "modem": [
            "Eski modemlerinizi internet sağlayıcınıza iade edin.",
            "Teknoloji projeleri için değerlendirin.",
            "Ev ağınızı yedek sistem olarak yapılandırın.",
            "Yazılım geliştirme projelerinde deney yapın."
        ],
        "kulaklık": [
            "Eski kulaklıklarınızı sanat projelerinde kullanabilirsiniz.",
            "Parçalarını ayırıp geri dönüşüm merkezine bırakın.",
            "DIY ses sistemlerinde yedek parça olarak değerlendirin.",
            "Kulaklık kablolarını elektronik projelerde kullanın."
        ],
        "router": [
            "Yedek internet bağlantısı olarak kullanabilirsiniz.",
            "Eski router'ı kablosuz erişim noktası olarak yapılandırın.",
            "Ağ projelerinde değerlendirin.",
            "OpenWRT gibi projeler için deney cihazına dönüştürün."
        ],
        "klavye": [
            "Tuşları el sanatları projelerinde kullanabilirsiniz.",
            "Elektronik atık merkezine teslim edin.",
            "Eski klavyeleri MIDI kontrol cihazı olarak yapılandırın.",
            "Eğitim projelerinde bilgisayar parçalarını incelemek için kullanın."
        ],
        "fare": [
            "Bilgisayar farelerini robot projelerinde kullanabilirsiniz.",
            "Parçalarını sanat projelerinde değerlendirin.",
            "Elektronik deneylerde sensör olarak kullanın.",
            "Geri dönüşüm kutularına bırakın."
        ]
    }

    tavsiye = geri_donusum_verileri.get(cihaz.lower(), ["Bu cihaz hakkında geri dönüşüm bilgisi bulunamadı."])
    await ctx.send(random.choice(geri_donusum_verileri))


@bot.command(name="yeniden_kullan")
async def yeniden_kullan(ctx, cihaz: str):
    yaratici_fikirler = {
        "telefon": [
            "Telefonunuzu müzik çalar olarak kullanın.",
            "Eski telefonunuzu çocuklar için eğitim cihazına dönüştürün.",
            "Ev otomasyon sistemine uzaktan kumanda olarak yapılandırın.",
            "Telefonunuzu güvenlik kamerasına dönüştürün."
        ],
        "tablet": [
            "Dijital resim çerçevesi olarak kullanabilirsiniz.",
            "Mutfakta tarif ekranı veya medya izleme cihazı yapın.",
            "Oyun emülatörü olarak kullanın.",
            "Kitap okuma cihazı olarak değerlendirin."
        ],
        "bilgisayar": [
            "NAS depolama sunucusu olarak kullanın.",
            "Yazılım geliştirme ve test projelerinde değerlendirin.",
            "Eğitim projeleri için sunucuya dönüştürün.",
            "Bilgisayar parçalarını DIY projelerde kullanın."
        ],
        "kamera": [
            "Eski kameraları güvenlik kamerası olarak kullanabilirsiniz.",
            "Canlı yayın ekipmanı yapabilirsiniz.",
            "Yaban hayatını izlemek için doğa kamerası yapabilirsiniz.",
            "Eğitim projelerine bağışlayın."
        ],
        "televizyon": [
            "Retro oyun konsollarını bağlamak için kullanın.",
            "Duvar ekranı olarak değerlendirin.",
            "Dijital sanat ekranına dönüştürün.",
            "Ev içi dijital tabela oluşturun."
        ],
        "hoparlör": [
            "Bluetooth hoparlör kitleri ile kablosuz hoparlör yapabilirsiniz.",
            "Ev sinema sistemine dönüştürün.",
            "Müzik stüdyosu ekipmanı olarak kullanın.",
            "Sanat projelerinde ses kabinleri yapın."
        ]
    }

    fikir = yaratici_fikirler.get(cihaz.lower(), ["Bu cihaz için yaratıcı kullanım önerisi bulunamadı."])
    await ctx.send(random.choice(fikir))


@bot.command(name="atik_azalt")
async def atik_azalt(ctx):
    ipuclar = [
        "Elektronik cihazlarınızı onarıp tekrar kullanmayı deneyin.",
        "Enerji tasarruflu cihazlar tercih edin.",
        "Gereksiz elektronik ürün satın almaktan kaçının.",
        "Eski şarj cihazlarınızı geri dönüşüm merkezine bırakın."
    ]
    await ctx.send(random.choice(ipuclar))


@bot.command(name="komutlar")
async def komutlar(ctx):
    komut_aciklamalari = {
        "!geri_donusum [cihaz]": "Bu komut, belirli bir cihaz için geri dönüşüm önerileri sunar.",
        "!yeniden_kullan [cihaz]": "Bu komut, belirli bir cihaz için yaratıcı yeniden kullanım önerileri sunar.",
        "!atik_azalt": "Bu komut, atıkları azaltmaya yönelik ipuçları sağlar.",
        "!komutlar": "Mevcut komutları ve açıklamalarını listeleyen komut."
    }
    
    mesaj = "Mevcut Komutlar ve Açıklamaları:\n"
    for komut, aciklama in komut_aciklamalari.items():
        mesaj += f"{komut}: {aciklama}\n"
    
    await ctx.send(mesaj)


TOKEN = "Tokenini Gir Kardes"
bot.run(TOKEN)
