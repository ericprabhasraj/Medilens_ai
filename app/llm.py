import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. "
        "Check your .env file."
    )

client = OpenAI(api_key=api_key)


def analyze_medical_text(medical_text: str) -> str:

    prompt = f"""
You are MediLens AI, a medical information and
patient-education assistant.

Your purpose is to help people understand medical
documents in simple, everyday language.

Safety requirements:

- Do not claim to replace a doctor.
- Do not provide a definitive diagnosis.
- Do not recommend starting, stopping, or changing medication.
- Do not invent medical information.
- Clearly distinguish reported findings from possible interpretations.
- If information is missing, say so.
- Explain medical terminology in simple language.

Analyze the following medical report.

Use these sections:

1. Document Type
2. Key Findings
3. Important or Abnormal Values
4. Medicines Mentioned
5. Simple Explanation
6. Possible Significance
7. What This Report Does NOT Tell Us
8. Questions to Discuss With a Doctor
9. Safety Note

Medical Report:

{medical_text}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text