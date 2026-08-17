# kvkk-uyum

**Kademe:** Tier A · **Dayanak:** 6698 sayılı Kişisel Verilerin Korunması Kanunu

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `aydinlatma-review` | Bir aydınlatma metnini KVKK m.10'un 5 zorunlu unsuru açısından denetler (veri sorumlusu kimliği, işleme amacı, alıcılar, toplama yöntemi/hukuki sebep, ilgili kişi hakları) |
| Skill | `acik-riza-denetimi` | Bir açık rıza metnini/formunu KVKK m.5'in 4 zorunlu unsuru açısından denetler; özellikle "paket rıza" ve "zımni rıza" geçersizlik risklerini önceliklendirir |
| Skill | `verbis-triyaji` | VERBİS kayıt yükümlülüğü ön triyajı (çalışan sayısı + mali bilanço kümülatif kriteri, özel nitelikli veri istisnası) — eşik değerlerin Kurul kararıyla değişebildiğini açıkça belirtir |

## Kurulum

```bash
claude plugin install kvkk-uyum@turkiye-legal
```

## Kullanım

```
/kvkk-uyum:aydinlatma-review [aydınlatma metni]
/kvkk-uyum:acik-riza-denetimi [rıza metni/formu]
/kvkk-uyum:verbis-triyaji [çalışan sayısı] [mali bilanço] [özel nitelikli veri mi]
```

`risk_level: high`, `requires_human_review: true` — çıktı her zaman bir avukat tarafından teyit edilmelidir.
