# Signaling Storm in 3GPP Documents

1. Download 3GPP files
2. unzip under './3GPP'
   ```
   find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
   ```
3. convert files to docx, Inside `./3GPP` run `convert.sh`
4. Inside the same directory with directory '3GPP', run `python3 search.py`
5. After obtaining the `res.pkl`, run `python3 generate_result.py > res.txt`
