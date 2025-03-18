# File Binary Converter

## Overview
This Python script allows users to:
1. Convert any file into a binary format.
2. Convert a binary file back into its original format.

## Features
- Supports all file types.
- Converts files to binary representation.
- Restores binary files to their original format.
- User-friendly command-line interface.

## Requirements
- Python 3.x

## Usage
### Convert a File to Binary
1. Run the script:  
   ```bash
   python file_binary_converter.py
   ```
2. Choose option `1`.
3. Enter the file name to convert.
4. The converted binary file will be saved with a `.bin` extension.

### Convert a Binary File Back to Original
1. Run the script:  
   ```bash
   python file_binary_converter.py
   ```
2. Choose option `2`.
3. Enter the binary file name.
4. Enter the desired output file name with its extension.

## Example
### Converting `document.pdf` to Binary
```
Enter your choice (1/2): 1
Enter the file to convert to binary: document.pdf
File 'document.pdf' has been converted to binary: 'document.pdf.bin'
```

### Restoring `document.pdf.bin` to Original
```
Enter your choice (1/2): 2
Enter the binary file to convert back: document.pdf.bin
Enter the output file name with extension: document_restored.pdf
Binary file 'document.pdf.bin' has been converted back to 'document_restored.pdf'
```

## License
This project is open-source and free to use.
