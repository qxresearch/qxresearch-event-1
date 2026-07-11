from pathlib import Path

import qrcode


def sanitize_filename(filename):
	candidate = filename.strip()

	if not candidate:
		raise ValueError("File name cannot be empty.")

	if "/" in candidate or "\\" in candidate:
		raise ValueError("File name must not contain path separators.")

	safe_name = Path(candidate).name
	if safe_name in {"", ".", ".."} or safe_name != candidate:
		raise ValueError("File name must be a simple name without path traversal.")

	return safe_name


def main():
	data = input("Enter some text or URL: ").strip()
	filename = sanitize_filename(input("Enter the file name: "))

	qr = qrcode.QRCode(box_size=10, border=5)
	qr.add_data(data)
	qr.make(fit=True)

	image = qr.make_image(fill_color="black", back_color="white")

	output_dir = Path(__file__).resolve().parent / "qr_images"
	output_dir.mkdir(exist_ok=True)

	output_path = output_dir / f"{filename}.png"
	image.save(output_path)

	print(f"QR code saved as {output_path}")


if __name__ == "__main__":
	main()

