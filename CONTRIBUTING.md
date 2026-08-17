# Katkı Süreci

Turkish Legal projesine katkıda bulunmak istediğiniz için teşekkürler! Bu belge, nasıl yardımcı olabileceğinizi açıklar.

## 🎯 Katkı Türleri

Aşağıdakilerin herhangi birinde katkıda bulunabilirsiniz:

1. **Yeni Skill**: Türk hukuku pratiğine yönelik yeni hukuki yetenekler
2. **Bug Düzeltme**: Mevcut skill'lerde hata düzeltmeleri
3. **Dokümantasyon**: README, API belgeler, örnekler
4. **Testler**: Golden eval senaryoları, regresyon testleri
5. **MCP Entegrasyonları**: Yeni veri kaynakları
6. **Optimizasyon**: Performans iyileştirmeleri

## 📋 Başlamadan Önce

- `CREDITS.md` okuyun
- [AGENTS.md](AGENTS.md) kurallarını inceleyin — mutlak sınırlar vardır
- `CREDITS.md` protokolünü anlayın

## 🚀 PR Adımları

### 1. Fork ve Clone

```bash
git clone https://github.com/YOUR_USERNAME/turkiye-legal.git
cd turkiye-legal
```

### 2. Branch Oluştur

```bash
git checkout -b feature/yeni-skill-adi
# veya
git checkout -b fix/hata-adi
```

### 3. Değişiklikleri Yap

#### Yeni Skill Eklemek İçin

```bash
# SKILL.md şablonunu kullanan yeni skill ekle
cat > <plugin>/skills/<skill-adi>/SKILL.md << 'YAML'
---
name: skill-adi-kebab-case
description: "Açıklama (max 200 char, öz ve net)"
user-invocable: true
turkiye_legal:
  version: 0.5.0
  category: litigation
  risk_level: medium  # low, medium, high, critical
  requires_human_review: false
  sources:
    - tur: kanun
      numara: "4721"  # TMK
      ad: "Türk Medeni Kanunu"
---

# Skill Adı

## Görev
- Amacı net olarak belirt

## Soğuk Başlangıç
1. İlk soru
2. İkinci soru

## Denetim Şeması
1. Adım 1
2. Adım 2

## Çıktı
- Çıktı örneği

## Kaynak Kuralı
- [DOĞRULANMADI] işareti yetersiz doğrulamaları belirtin
YAML
```

#### Yeni Kanun Eklemek İçin

Önce `sources/mevzuat/kanunlar.yaml`'a ekleyin:

```yaml
  - numara: "6284"
    ad: "Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun"
    kabul_tarihi: "2010-01-08"
    rg_tarih_sayi: "21.01.2010 / 27531"
    dogrulama_url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6284.pdf"
    durum: "yururlukte"
    son_dogrulama: "2024-01-15 (resmî kaynak doğrulandı)"
```

### 4. Doğrulamayı Çalıştır

```bash
source .venv/bin/activate
python3 scripts/validate/validate_skills.py --strict
python3 scripts/validate/validate_sources.py
python3 scripts/validate/lint_prompts.py
```

Tüm testlerin **PASS** olması gerekir.

### 5. Commit Yapın

```bash
git add <files>
git commit -s -m "Kısa başlık

Daha ayrıntılı açıklama eğer gerekli ise.

Düzeltme: #123"
```

**Önemli**: `-s` flag'i ile commit yapın (DCO imzası).

### 6. Push ve PR

```bash
git push origin feature/yeni-skill-adi
```

GitHub'a gidin ve PR oluşturun:
- **Base**: `main`
- **Title**: Kısa, açıklayıcı
- **Body**:
  ```
  ## Özet
  - Yeni skill: X
  - Düzeltme: Y
  
  ## Test Planı
  - [ ] SKILL.md frontmatter doğrulandı
  - [ ] validate_sources.py geçti
  - [ ] Skill manuel olarak test edildi
  
  Closes #123
  ```

## ✅ Kabul Kriterleri

PR'ınız şunları içermeli:

- ✅ Tüm testler geçer (`validate_*` 100% PASS)
- ✅ Yeni kanun referansı varsa, önce `kanunlar.yaml`'a eklendi
- ✅ Doğrulanamayan bilgi `[DOĞRULANMADI]` ile işaretlendi
- ✅ AGENTS.md mutlak sınırları ihlal etmez
- ✅ Description: maksimum 200 karakter, öz
- ✅ Commit'ler DCO imzalı (`git commit -s`)

## 🚫 Kabul Edilmez

Aşağıdakiler PR reddedilebilir:

- ❌ Uydurma kanun/karar numarası
- ❌ Eski marka izleri — tüm adlandırma `turkiye-legal` olmalıdır
- ❌ Validation hataları
- ❌ Dokümantasyon olmayan kod
- ❌ DCO imzası olmayan commit'ler

## 📚 Kaynaklar

- [Türk Medeni Kanunu](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=4721)
- [mevzuat.gov.tr](https://www.mevzuat.gov.tr)
- [Yargıtay Kararları](https://karararama.yargitay.gov.tr)
- [Danıştay Kararları](https://karararama.danistay.gov.tr)

## ❓ Sorular?

- GitHub [Discussions](https://github.com/mesutcandemir39/turkiye-legal/discussions) açın
- `CREDITS.md` oku
- Mevcut skill'leri örnek olarak incele

---

**Teşekkür ederiz!** 🇹🇷 ⚖️ 🤖
