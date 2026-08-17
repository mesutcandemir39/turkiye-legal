# [DOĞRULANMADI] Protokolü

Tüm `turkiye-legal` skill'leri bu protokole uyar. Amaç: model kendi eğitim verisinden konuştuğunda bunu **açıkça** işaretlemek — bkz. `ADR-005`.

## Kural

Bir skill, aşağıdaki iki koşuldan **biri** karşılanmadan bir hukuki iddiada bulunuyorsa, o iddiayı `[DOĞRULANMADI]` etiketiyle işaretlemek zorundadır:

1. İddia, `sources/mevzuat/kanunlar.yaml` (veya ileride eklenecek `sources/ictihat/`, `sources/kurumsal/`) kayıt defterinde doğrulanmış bir kaynağa dayanıyor, **veya**
2. Kullanıcının kendisi bu bilgiyi girdi olarak sağlamış (örn. kullanıcı bir karar numarası verip "bu kararı özetle" diyor — bu durumda skill kararı üretmiyor, kullanıcının verdiğini işliyor).

## Format

```
[DOĞRULANMADI] Bu konuda güncel bir düzenleme olduğunu hatırlıyorum ancak
bunu kayıt defterimizde doğrulayamadım. Lütfen mevzuat.gov.tr veya resmî
bir kaynaktan teyit edin.
```

## Neden bu gerekli

Bir dil modeli, eğitim verisindeki bir kanunu güncel zannedip yürürlükten kalkmış bir hükmü doğruymuş gibi sunabilir, ya da bir madde numarasını yanlış hatırlayabilir. `[DOĞRULANMADI]` etiketi, kullanıcının (özellikle bir avukatın) bu riski görmesini ve kendi doğrulamasını yapmasını sağlar — bu, projenin "insan-in-the-loop" ilkesinin (README "Hukuki Sorumluluk Reddi") somut uygulamasıdır.

## Bu etiket ne zaman KULLANILMAZ

- Kayıt defterinde doğrulanmış bir kaynağa atıf yapılırken (o zaman doğrudan kaynak gösterilir, `[DOĞRULANMADI]` gerekmez).
- Genel hukuki kavram açıklamalarında (örn. "sözleşme" kelimesinin anlamı) — bunlar doğrulama gerektirmeyecek kadar temel kavramlardır.
- Kullanıcının kendi verdiği bilgiyi tekrarlarken.
