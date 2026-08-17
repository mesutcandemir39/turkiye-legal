# sozlesme

**Kademe:** Tier A · **Dayanak:** 6098 sayılı Türk Borçlar Kanunu

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `riskli-hukum-taramasi` | Sözleşmedeki genel işlem koşullarını (GİK) tespit eder, TBK m.20-21 kapsamında "yazılmamış sayılma" riski taşıyan hükümleri işaretler |
| Skill | `kira-sozlesmesi-kontrolu` | Konut/çatılı işyeri kira sözleşmesini denetler: güvence bedeli (depozito) üç aylık kira bedeli sınırı (m.342), saklanma usulü |
| Skill | `gizlilik-hizmet-sozlesmesi-taramasi` | Gizlilik (NDA) ve hizmet/danışmanlık sözleşmelerinde aşırı cezai şart (TBK m.182) ve ölçüsüz gizlilik/rekabet yasağı kapsamını işaretler |

## Kurulum

```bash
claude plugin install sozlesme@turkiye-legal
```

## Kullanım

```
/sozlesme:riskli-hukum-taramasi [sözleşme metni]
/sozlesme:kira-sozlesmesi-kontrolu [kira sözleşmesi metni]
/sozlesme:gizlilik-hizmet-sozlesmesi-taramasi [NDA veya hizmet sözleşmesi metni]
```

`risk_level: high`, `requires_human_review: true` — bu bir ön taramadır, imza kararı bir avukat görüşü gerektirir.
