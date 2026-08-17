#!/usr/bin/env python3
"""
Real-Time Source Validation Engine
Hiçbir atıf sessizce geçmez.
"""

import re
import json
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime

# ==================== DATA MODELS ====================

class ValidationStatus(Enum):
    VERIFIED = "✅"
    UNCERTAIN = "⚠️"
    ABROGATED = "⚠️"
    NOT_FOUND = "❌"
    INVALID = "❌"
    ERROR = "❌"

class FlagColor(Enum):
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"

@dataclass
class Citation:
    """Atıf (Karar numarası veya Kanun maddesi)"""
    type: str  # "court_decision" veya "law_article"
    original_text: str
    year: str = None
    court: str = None
    chamber: str = None
    number: str = None
    law_code: str = None
    article: str = None

@dataclass
class ValidationResult:
    status: ValidationStatus
    citation: Citation
    confidence: float = 1.0
    message: str = ""
    source: str = "mevzuat.adalet.gov.tr"
    data: Dict = None
    similar_records: List[Dict] = None
    timestamp: str = None

@dataclass
class Flag:
    color: FlagColor
    icon: str
    message: str
    confidence: float = 1.0

# ==================== CITATION EXTRACTOR ====================

class CitationExtractor:
    """AI yanıtından atıfları çıkar."""

    @staticmethod
    def extract(text: str) -> List[Citation]:
        """Metinden tüm atıfları çıkar."""
        citations = []

        # Pattern 1: Yargıtay Kararları
        # Örnek: 2024-Y-3D/123456, 2023-Y-1D-KG/9844
        yargitay_pattern = r'(\d{4})-Y-(\d+)([A-Z])?(?:-([A-Z]+))?/(\d+)'
        for match in re.finditer(yargitay_pattern, text):
            citations.append(Citation(
                type="court_decision",
                original_text=match.group(0),
                year=match.group(1),
                chamber=match.group(2),
                court="Yargıtay",
                number=match.group(5)
            ))

        # Pattern 2: Danıştay Kararları
        # Örnek: 2024-D-3/123456
        danistay_pattern = r'(\d{4})-D-(\d+)/(\d+)'
        for match in re.finditer(danistay_pattern, text):
            citations.append(Citation(
                type="court_decision",
                original_text=match.group(0),
                year=match.group(1),
                court="Danıştay",
                chamber=match.group(2),
                number=match.group(3)
            ))

        # Pattern 3: Kanun Maddeleri
        # Örnek: TMK m.174, TCK m.213, "TBK m.20/1"
        law_pattern = r'([A-Z]{1,4})\s+m\.(\d+(?:/\d+)?)'
        for match in re.finditer(law_pattern, text):
            citations.append(Citation(
                type="law_article",
                original_text=match.group(0),
                law_code=match.group(1),
                article=match.group(2)
            ))

        return citations

# ==================== SOURCE VALIDATOR ====================

class SourceValidator:
    """Atıfları veritabanında doğrula."""

    def __init__(self):
        # Mock databases (gerçekte mevzuat.adalet.gov.tr API'ye bağlanacak)
        self.yargitay_decisions = self._load_yargitay_mock()
        self.law_database = self._load_laws_mock()

    def _load_yargitay_mock(self) -> Dict:
        """Mock Yargıtay veritabanı."""
        return {
            "2024-Y-1D/9844": {
                "year": 2024,
                "chamber": "1",
                "type": "decision",
                "status": "published",
                "date": "2024-08-15",
                "subject": "Tazminat Hakkı"
            },
            "2023-Y-3D/8765": {
                "year": 2023,
                "chamber": "3",
                "type": "decision",
                "status": "published",
                "date": "2023-06-20",
                "subject": "Boşanma"
            }
        }

    def _load_laws_mock(self) -> Dict:
        """Mock Mevzuat Veritabanı."""
        return {
            "TMK": {
                "name": "Türk Medeni Kanunu",
                "number": "4721",
                "articles": {
                    "174": {
                        "text": "Tazminat hakkı...",
                        "status": "active",
                        "last_update": "2023-07-14",
                        "amendment_history": ["2023-07-14 (7431)"]
                    },
                    "175": {
                        "text": "Yoksulluk nafakası...",
                        "status": "active",
                        "last_update": "2023-07-14"
                    }
                }
            },
            "TCK": {
                "name": "Türk Ceza Kanunu",
                "number": "5237",
                "articles": {
                    "212": {"text": "Hırsızlık...", "status": "active"},
                    "213": {"text": "MÜLGA", "status": "abrogated", "reason": "TCK m.212'ye dahil"}
                }
            }
        }

    def validate_decision(self, citation: Citation) -> ValidationResult:
        """Karar numarasını doğrula."""

        # Format kontrolü
        if not citation.year or not citation.chamber or not citation.number:
            return ValidationResult(
                status=ValidationStatus.INVALID,
                citation=citation,
                message="Karar numarası formatı yanlış",
                timestamp=datetime.now().isoformat()
            )

        # Veritabanı araması
        key = f"{citation.year}-Y-{citation.chamber}/{citation.number}"

        if key in self.yargitay_decisions:
            data = self.yargitay_decisions[key]
            return ValidationResult(
                status=ValidationStatus.VERIFIED,
                citation=citation,
                confidence=1.0,
                data=data,
                message=f"✅ Doğrulandı: {data['date']} - {data['subject']}",
                timestamp=datetime.now().isoformat()
            )

        # Benzer karar araması
        similar = self._find_similar_decisions(citation)

        if similar:
            return ValidationResult(
                status=ValidationStatus.UNCERTAIN,
                citation=citation,
                confidence=0.6,
                similar_records=similar,
                message=f"⚠️ Tam eşleşme yok, benzer: {similar[0]}",
                timestamp=datetime.now().isoformat()
            )

        # Bulunamadı
        return ValidationResult(
            status=ValidationStatus.NOT_FOUND,
            citation=citation,
            confidence=0.0,
            message="❌ Veritabanında bulunamadı",
            timestamp=datetime.now().isoformat()
        )

    def validate_law_article(self, citation: Citation) -> ValidationResult:
        """Kanun maddesini doğrula."""

        # Kanun bulma
        law_code = citation.law_code.upper()

        if law_code not in self.law_database:
            return ValidationResult(
                status=ValidationStatus.NOT_FOUND,
                citation=citation,
                message=f"❌ '{law_code}' kanunu bulunamadı",
                timestamp=datetime.now().isoformat()
            )

        law = self.law_database[law_code]

        # Madde kontrol
        if citation.article not in law["articles"]:
            return ValidationResult(
                status=ValidationStatus.NOT_FOUND,
                citation=citation,
                message=f"❌ {law_code} m.{citation.article} bulunamadı",
                timestamp=datetime.now().isoformat()
            )

        article = law["articles"][citation.article]

        # Yürürlük kontrol
        if article["status"] == "abrogated":
            return ValidationResult(
                status=ValidationStatus.ABROGATED,
                citation=citation,
                message=f"⚠️ Madde mülga: {article.get('reason', 'Sebep belirtilmemiş')}",
                data=article,
                timestamp=datetime.now().isoformat()
            )

        # Başarı
        return ValidationResult(
            status=ValidationStatus.VERIFIED,
            citation=citation,
            confidence=1.0,
            data=article,
            message=f"✅ Doğrulandı: {law['name']} m.{citation.article}",
            timestamp=datetime.now().isoformat()
        )

    def _find_similar_decisions(self, citation: Citation) -> List[str]:
        """Benzer karar ara."""
        similar = []

        for key in self.yargitay_decisions.keys():
            # Aynı daire, fakat farklı numara
            if f"-Y-{citation.chamber}/" in key and key != citation.original_text:
                similar.append(key)

        return similar[:3]  # En fazla 3 benzer

# ==================== FLAG GENERATOR ====================

class FlagGenerator:
    """Doğrulama sonucunu flag'e çevir."""

    @staticmethod
    def generate(validation: ValidationResult) -> Flag:
        """ValidationResult'ı Flag'e çevir."""

        if validation.status == ValidationStatus.VERIFIED:
            return Flag(
                color=FlagColor.GREEN,
                icon="✅",
                message="Doğrulandı",
                confidence=validation.confidence
            )

        elif validation.status in [ValidationStatus.UNCERTAIN, ValidationStatus.ABROGATED]:
            return Flag(
                color=FlagColor.YELLOW,
                icon="⚠️",
                message="Şüpheli — Doğrulama önerilir",
                confidence=validation.confidence
            )

        else:  # NOT_FOUND, INVALID, ERROR
            return Flag(
                color=FlagColor.RED,
                icon="❌",
                message="Doğrulanamadı — Avukat kontrol gerekli",
                confidence=0.0
            )

# ==================== MAIN VALIDATOR ====================

class RealTimeValidator:
    """Ana validator: Metni doğrula ve yanıtı zenginleştir."""

    def __init__(self):
        self.extractor = CitationExtractor()
        self.validator = SourceValidator()
        self.flag_generator = FlagGenerator()

    def validate_response(self, ai_response: str) -> Tuple[str, Dict]:
        """
        AI yanıtını doğrula ve flag'lerle zenginleştir.

        Return:
            (modified_response, validation_report)
        """

        # Atıfları çıkar
        citations = self.extractor.extract(ai_response)

        if not citations:
            return ai_response, {"citations_found": 0, "status": "OK"}

        # Her atıfı doğrula
        validations = []
        flags_dict = {}

        for citation in citations:
            if citation.type == "court_decision":
                validation = self.validator.validate_decision(citation)
            else:
                validation = self.validator.validate_law_article(citation)

            validations.append(validation)
            flag = self.flag_generator.generate(validation)
            flags_dict[citation.original_text] = flag

        # Yanıtı flag'lerle zenginleştir
        modified = ai_response
        for citation_text, flag in flags_dict.items():
            pattern = re.escape(citation_text)
            replacement = f"{citation_text} {flag.icon}"
            modified = re.sub(pattern, replacement, modified)

        # RED flag varsa başa uyarı ekle
        red_flags = [v for v in validations if v.status == ValidationStatus.NOT_FOUND]

        if red_flags:
            warning = f"""
🛑 UYARI: Bu yanıtta doğrulanamayan referans var:
{chr(10).join(f"  • {v.message}" for v in red_flags[:3])}

ÖNERILEN İŞLEM: Avukatla teyit alınız.
{"─" * 60}

"""
            modified = warning + modified

        # Rapor oluştur
        report = {
            "timestamp": datetime.now().isoformat(),
            "citations_found": len(citations),
            "validations": [asdict(v) for v in validations],
            "status": "CRITICAL" if red_flags else ("WARNING" if any(
                v.status == ValidationStatus.UNCERTAIN for v in validations
            ) else "OK")
        }

        return modified, report

# ==================== TEST ====================

def main():
    """Validator'ı test et."""

    validator = RealTimeValidator()

    # Test yanıtı
    test_response = """
    TMK m.174'e göre tazminat hakkı, boşanma sırasında kusurlu olmayan tarafın
    haklarını korur. Yargıtay 2024-Y-1D/9844 kararında bu maddenin uygulanışını
    belirtmiştir. Ayrıca TCK m.213 hakkında danışman alınız.
    """

    print("=" * 70)
    print("REAL-TIME VALIDATION ENGINE TEST")
    print("=" * 70)
    print("\n📝 Orijinal Yanıt:")
    print(test_response)

    # Doğrula
    modified, report = validator.validate_response(test_response)

    print("\n✅ Doğrulanmış Yanıt:")
    print(modified)

    print("\n📊 Doğrulama Raporu:")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    print("\n" + "=" * 70)
    print(f"Durum: {report['status']}")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
