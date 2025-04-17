# 🧠 Project FRA - Sonic Proximity Score (SPS) Model v1.2

This Python library computes a "Sonic Proximity Score" (SPS) between IPA phonemes using a vector-based articulatory feature model.

### 🆕 Version 1.2
- ✅ Refactored distance formula: `SPS = 1 - (d / d_max)`
- ✅ Added non-pulmonic consonants: clicks, implosives, ejectives
- ✅ Supports consonants and vowels in a unified interface

---

## 🛠 How to Use

```bash
git clone https://github.com/yourusername/fra-sps-model.git
cd fra-sps-model
python3 sps_model/interactive_tool.py
