import os

OLD_TEXT = "koeleothan"
NEW_TEXT = "mem_koeleothan"
DRY_RUN = False  # Set to False to actually rename files


def rename_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if OLD_TEXT in filename:
                old_path = os.path.join(root, filename)
                new_filename = filename.replace(OLD_TEXT, NEW_TEXT)
                new_path = os.path.join(root, new_filename)

                if old_path != new_path:
                    print(f"{old_path} -> {new_path}")
                    if not DRY_RUN:
                        os.rename(old_path, new_path)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rename_files(base_dir)
