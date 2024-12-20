import shutil
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path")
    parser.add_argument("zip_path")

    args = parser.parse_args()
    shutil.make_archive(args.zip_path, 'zip', args.folder_path)
