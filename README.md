# Signaling Storm in 3GPP Documents

1. Download 3GPP files
2. unzip
   ```
   find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
   ```
3. convert files to docx
   ```
   Inside `./3GPP`, run `convert.sh`
