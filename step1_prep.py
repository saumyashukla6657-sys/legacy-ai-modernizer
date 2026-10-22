import os

def load_and_index_code(file_path: str) -> str:
    """Reads a source file and prefixes every line with a 4-digit line index."""
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found!"

    with open(file_path, "r") as f:
        raw_lines = f.readlines()
    
    indexed_lines = []
    for idx, line in enumerate(raw_lines, start=1):
        # Attach line numbers: '0001 | code'
        indexed_lines.append(f"{idx:04d} | {line.rstrip()}")
    
    return "\n".join(indexed_lines)

if __name__ == "__main__":
    file_target = "data/sample_loan.cob"
    annotated_code = load_and_index_code(file_target)
    print("--- PREPARED SOURCE CODE WITH LINE NUMBERS ---")
    print(annotated_code)