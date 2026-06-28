import os


def rename_files(folder, prefix):
    if not os.path.exists(folder):
        raise FileNotFoundError("Folder does not exist.")

    files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

    count = 0

    for index, file in enumerate(files, start=1):
        old_path = os.path.join(folder, file)

        extension = os.path.splitext(file)[1]

        new_name = f"{prefix}_{index}{extension}"

        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

        count += 1

    return count
