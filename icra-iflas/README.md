# icra-iflas

**Kademe:** Tier A · **Dayanak:** 2004 sayılı İcra ve İflas Kanunu

2004 sayılı İcra ve İflas Kanunu kapsamında dosya triyajı, itiraz ve şikâyet süre analizi sağlayan eklenti.

## İçerik

| Tür | Ad | Ne yapar |
|---|---|---|
| Skill | `icra-dosya-triyaji` | Ödeme emrine itiraz (m.62, 7 gün) veya icra dairesi işlemine şikâyet (m.16, 7 gün) süresinin son tarihini hesaplar |
| Skill | `haciz-ihbarnamesi-triyaji` | Haciz ihbarnamesinin (m.89) sırasına göre (1./2./3. ihbarname) doğru başvuru yolunu (icra müdürlüğüne itiraz veya menfi tespit davası) ve süresini belirler |

## Kurulum

```bash
claude plugin install icra-iflas@turkiye-legal
```

## Kullanım

```
/icra-iflas:icra-dosya-triyaji [tebliğ/öğrenme tarihi] [belge türü]
/icra-iflas:haciz-ihbarnamesi-triyaji [tebliğ tarihi] [ihbarname sırası]
```

`risk_level: critical` — bu iki süre de yedişer gün gibi kısa ve kolayca kaçırılabilir. **Not:** İçerdiği süre bilgileri tek kaynaktan doğrulanmıştır; ikinci bağımsız kaynak teyidi bekliyor (bkz. `references/itiraz_sikayet_sureleri.yaml`).
