# test_setup.py
import sys


def check_setup():
    print(f"Python version: {sys.version}")

    # Check libraries one by one
    try:
        import numpy
        print("numpy version:", numpy.__version__)
    except ImportError:
        print("numpy not found")

    try:
        import pandas
        print("pandas version:", pandas.__version__)
    except ImportError:
        print("pandas not found")

    try:
        import sklearn
        print("scikit-learn version:", sklearn.__version__)
    except ImportError:
        print("scikit-learn not found")

    try:
        import nltk
        print("nltk version:", nltk.__version__)
        # Don't try to download here
    except ImportError:
        print("nltk not found")

    print("\nBasic library check complete!")


if __name__ == "__main__":
    check_setup()
