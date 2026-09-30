from src.ingestion.source_1 import source_1
from src.ingestion.source_2 import source_2
from src.transform.transform import transform
from src.validation.source import validate_and_save


def main():

    print("\n========== NEWS DATA PIPELINE ==========\n")

    print("Process 1: Ingestion - Source 1")
    source_1()
    print("Process 1: Complete ✓\n")

    print("Process 2: Ingestion - Source 2")
    source_2()
    print("Process 2: Complete ✓\n")

    print("Process 3: Validation")
    validate_and_save()
    print("Process 3: Complete ✓\n")

    print("Process 4: Transformation")
    transform()
    print("Process 4: Complete ✓\n")

    print("========== PIPELINE COMPLETE ==========\n")


if __name__ == "__main__":
    main()