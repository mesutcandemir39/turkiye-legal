---
name: resmi-gazete-gunluk
description: "Her sabah Resmî Gazete'yi kontrol edip değişiklikleri hukukçulara özetleyen zamanlanmış rutin."
schedule: "günlük, 07:00 UTC (bkz. .github/workflows/scheduled-maintenance.yml)"
status: NOT_IMPLEMENTED
---

# Resmî Gazete Günlük Kontrolü (Agent)

## Durum: NOT_IMPLEMENTED

Bu agent'ın **çalışma mantığı ve LLM talimatı** aşağıda tanımlıdır, ancak henüz gerçek bir Resmî Gazete kaynağına (API/RSS/web scraping) bağlı **değildir**. `.github/workflows/scheduled-maintenance.yml` şu an bu agent'ı simüle eden bir `[SIMULATED]` issue açar — bkz. o dosyadaki yorum. Layer 5 (Connectors) kapsamındadır ve `CREDITS.md`'de "v0.1.0'de yalnız arayüz" olarak işaretlenmiştir.

Bu dosyanın burada bulunma amacı: bağlantı eklendiğinde (ROADMAP Q3) agent'ın nasıl davranması gerektiğini önceden belirlemek, böylece bir katkıcı yalnızca connector'ı bağlayıp bu mantığı aktifleştirebilir.

## Pipeline (bağlantı eklendiğinde çalışacak)

```
Resmî Gazete kaynağı → Yeni sayı tespiti → sources/mevzuat/ ile karşılaştırma
  → Değişen/yeni kanunları işaretle → mevzuat-degisiklik-analizi skill'ini çağır
  → Özet raporu üret → İnsan onayına sun (issue veya bildirim olarak)
```

## LLM Talimatı (connector bağlandığında kullanılacak sistem promptu)

```
Sen bir mevzuat takip asistanısın. Sana bugünkü Resmî Gazete'nin içeriği
(başlıklar ve varsa tam metinler) verilecek.

Görevin:
1. Yeni yayımlanan kanun, CBK, yönetmelik, tebliğ var mı tespit et.
2. Bunlardan hangileri sources/mevzuat/kanunlar.yaml defterindeki mevcut
   kayıtları etkiliyor (değiştiriyor/yürürlükten kaldırıyor) tespit et.
3. Her biri için 2-3 cümlelik bir özet yaz: ne değişti, kimi etkiliyor.
4. SAKIN yeni bir kanun numarası veya madde numarası UYDURMA — yalnızca
   sana verilen Resmî Gazete içeriğinde GERÇEKTEN geçen bilgiyi kullan.
5. Eğer içerik belirsizse veya emin değilsen, o maddeyi [DOĞRULANMADI]
   olarak işaretle.
6. Çıktının sonuna: "Bu özet otomatik üretilmiştir, resmî metin ile
   karşılaştırılarak teyit edilmelidir" uyarısını ekle.
```

## Bağlanacak connector için gereksinimler (Faz sonrası)

- Kaynak: Resmî Gazete'nin güncel yayın API'si veya RSS akışı (henüz seçilmedi)
- Kimlik doğrulama: gerekiyorsa `.mcp.json` üzerinden yapılandırılacak
- Çıktı formatı: bu agent'ın ürettiği özet, `sources/mevzuat/kanunlar.yaml`'a yeni kayıt eklenmesi için bir PR taslağına dönüştürülebilir (ama otomatik commit ATILMAZ — insan onayı zorunludur, bkz. `.claude/CLAUDE.md` güvenlik sınırları)
