import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schemas import ModernizationArtifact
from step1_prep import load_and_index_code

# Load environment variables
load_dotenv()

def extract_modernization_evidence(file_path: str) -> ModernizationArtifact:
    annotated_code = load_and_index_code(file_path)

    # Use the active recommended model
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    structured_llm = llm.with_structured_output(ModernizationArtifact)

    prompt = f"""
    You are an enterprise legacy system modernization architect.
    Analyze the following line-numbered COBOL source code.
    
    CRITICAL AUDIT INSTRUCTIONS:
    - Extract all decision paths and business rules.
    - Every rule MUST accurately quote the exact line numbers (e.g., '0012-0013') where the logic occurs.
    - Identify migration risks such as hardcoded threshold values, missing edge-case validations, or rigid batch patterns.
    - Do not invent code that is not present.

    SOURCE CODE:
    {annotated_code}
    """

    print("Analyzing legacy code with Gemini 3.8 Flash...")
    result = structured_llm.invoke(prompt)
    return result

if __name__ == "__main__":
    artifact = extract_modernization_evidence("data/sample_loan.cob")
    print("\n--- EXTRACTION SUCCESSFUL ---")
    print(artifact.model_dump_json(indent=2))