"""
Merge all PDF files in the current working directory into a single output file
named Final_pdf.pdf, then remove the original PDF files except for the merged
output.
"""

import os
from pypdf import PdfWriter  # pypdf replaces the abandoned PyPDF4


def get_pdf_files():
    """Return sorted list of PDF files in cwd, excluding the output file."""
    return sorted([
        f for f in os.listdir()
        if f.endswith('.pdf') and f != 'Final_pdf.pdf'
    ])


def merge_pdfs(output_name='Final_pdf.pdf'):
    pdf_files = get_pdf_files()

    # Guard: nothing to merge
    if not pdf_files:
        print("❌ No PDF files found in the current directory.")
        return

    print(f"📄 Found {len(pdf_files)} PDF(s) to merge:")
    for f in pdf_files:
        print(f"   - {f}")

    # Guard: output already exists
    if os.path.exists(output_name):
        overwrite = input(f"\n⚠️  '{output_name}' already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Aborted.")
            return

    # Merge
    writer = PdfWriter()
    try:
        for pdf in pdf_files:
            writer.append(pdf)
            print(f"✅ Appended: {pdf}")

        with open(output_name, 'wb') as out:
            writer.write(out)

        print(f"\n🎉 Merged PDF saved as '{output_name}'")

    except Exception as e:
        print(f"❌ Merge failed: {e}")
        return  # Don't delete originals if merge failed

    finally:
        writer.close()

    # Confirm before deleting originals
    confirm = input(f"\n⚠️  Delete the {len(pdf_files)} original PDF(s)? (y/n): ")
    if confirm.lower() == 'y':
        for pdf in pdf_files:
            os.remove(pdf)
            print(f"🗑️  Deleted: {pdf}")
    else:
        print("✅ Original files kept.")


if __name__ == '__main__':
    merge_pdfs()