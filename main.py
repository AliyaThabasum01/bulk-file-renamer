from renamer import rename_files

print("=" * 50)
print("📂 Bulk File Renamer")
print("=" * 50)

folder = input("\nEnter folder path: ")
prefix = input("Enter new filename prefix: ")

try:
    total = rename_files(folder, prefix)
    print(f"\n✅ Successfully renamed {total} file(s).")

except Exception as e:
    print("\n❌ Error:", e)
