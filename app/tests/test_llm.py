from app.llm import analyze_medical_text


sample_report = """
Patient blood test:

Hemoglobin: 10.2 g/dL
Reference range: 12-16 g/dL

WBC: 7,500 /µL
Reference range: 4,000-11,000 /µL

Platelets: 250,000 /µL
Reference range: 150,000-450,000 /µL
"""


result = analyze_medical_text(sample_report)

print("\n========== MEDILENS AI ==========\n")
print(result)
print("\n=================================\n")