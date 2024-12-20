# Image Pipeline

## Project Overview
This project automates the image processing workflow, enabling the downloading, processing, and delivery of images via email. The pipeline includes the following steps:

1. **Download Images**: Retrieve images from online sources based on a specified keyword.
2. **Convert to Grayscale**: Transform images to grayscale for simplified processing.
3. **Resize Images**: Scale images by a specified percentage to reduce their size.
4. **Compress Files**: Archive processed images into a ZIP file for easier sharing.
5. **Send Email**: Send the ZIP file as an email attachment to a specified recipient.

The pipeline can be customized or run using predefined configurations for common use cases.

---

## Features


#### **Usage**
Run the script with the following syntax:

```bash
python main.py <keyword> <max_num> <downstorage_dir> <constorage_dir> <scale_percent> <scstorage_dir> <zipstorage_dir> <recipient_email>
```

#### **Parameters**
- `<keyword>`: The search keyword for images.
- `<max_num>`: The maximum number of images to download.
- `<downstorage_dir>`: Directory to store the downloaded images.
- `<constorage_dir>`: Directory to save the grayscale images.
- `<scale_percent>`: Percentage to resize the images.
- `<scstorage_dir>`: Directory to save the resized images.
- `<zipstorage_dir>`: Path where the ZIP file will be saved (without file extension).
- `<recipient_email>`: Recipient's email address.

#### **Example**
To process images of "cats" with 10 downloads, resize them to 50%, and send the ZIP file to `recipient@example.com`:

```bash
python pipeline.py cats 10 cats_images cats_images_greyscale 50 cats_images_scaled cats_images_archive recipient@example.com
```

---

### **Predefined Script (`main.py`)**
The `main.py` script provides a streamlined approach with predefined parameters.

#### **Workflow**
1. Downloads 20 images of "motorbike" into the `output1` directory.
2. Converts the images to grayscale and saves them in the `output2` directory.
3. Resizes the grayscale images to 50% and saves them in the `output3` directory.
4. Compresses the resized images into a ZIP file named `Finalzip.zip`.
5. Sends the ZIP file to `email@email.com`.

#### **Usage**
Simply run the script:

```bash
python simplepipe.py
```

---

## Requirements

### **Prerequisites**
- Python 3.7+
- Required Python packages:
  - `icrawler`
  - `Pillow`
  - `argparse`
  - `yagmail`

### **Installation**
Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

---

## Step-by-Step Execution
If you prefer running each step of the pipeline individually, use the following scripts:

1. **Download Images**:
   ```bash
   python src/download.py <max_num> <keyword> <output_folder1>
   ```

2. **Convert to Grayscale**:
   ```bash
   python src/convertToGrayScale.py <output_folder1> <output_folder2>
   ```

3. **Resize Images**:
   ```bash
   python src/scale.py <output_folder2> <output_folder3>
   ```

4. **Compress Files**:
   ```bash
   python src/zip.py <output_folder3> <zip_name>
   ```

5. **Send Email**:
   ```bash
   python src/send.py <zip_file_path> <recipient_email>
   ```

---


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

