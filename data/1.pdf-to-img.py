# import module
from pdf2image import convert_from_path
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PDF to Image')
    parser.add_argument('--pdf-dir', type=str, help='Path to data directory with PDF files')
    parser.add_argument('--out-dir', type=str, help='Path to data directory to save images')
    args = parser.parse_args()

    pdf_dir = args.pdf_dir
    out_dir = args.out_dir

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            print("Processing: ", pdf_file)
            images = convert_from_path(os.path.join(pdf_dir, pdf_file))
            for i in range(len(images)):
                images[i].save(os.path.join(out_dir, pdf_file + '_page'+ str(i) +'.jpg'), 'JPEG')
