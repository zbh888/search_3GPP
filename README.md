# Signaling Storm in 3GPP Documents

1. Download 3GPP files
2. unzip
   ```
   find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
   ```
3. convert files to docx
   ```
   lowriter --convert-to docx *.doc
   ```

```{bash}
#!/bin/bash

echo "Directory: $(pwd)"

for dir in */; do
    cd "$dir" || exit
    for dirr in */; do
        cd "$dirr" || exit
        echo "Directory: $(pwd)"
        cd ..
    done
    cd ..
done
```
