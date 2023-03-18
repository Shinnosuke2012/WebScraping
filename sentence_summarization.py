from transformers import pipeline

#import model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE= """
Recently, interest in aluminium ion batteries with aluminium anodes, graphite cathodes and ionic liquid electrolytes has increased; however, much remains to be done to increase the cathode capacity and to understand details of the anion–graphite intercalation mechanism. Here, an aluminium ion battery cell made using pristine natural graphite flakes achieves a specific capacity of ∼110 mAh g−1 with Coulombic efficiency ∼98%, at a current density of 99 mA g−1 (0.9 C) with clear discharge voltage plateaus (2.25–2.0 V and 1.9–1.5 V). The cell has a capacity of 60 mAh g−1 at 6 C, over 6,000 cycles with Coulombic efficiency ∼ 99%. Raman spectroscopy shows two different intercalation processes involving chloroaluminate anions at the two discharging plateaus, while C–Cl bonding on the surface, or edges of natural graphite, is found using X-ray absorption spectroscopy. Finally, theoretical calculations are employed to investigate the intercalation behaviour of choloraluminate anions in the graphite electrode.
"""

summary = summarizer(ARTICLE, max_length=100, min_length=50, do_sample=False)[0]
print(summary["summary_text"])