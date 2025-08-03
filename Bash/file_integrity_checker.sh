#!/bin/bash

echo "[*] Enter the target directory to check:"
read -r target_dir

hash_file="file_hashes.txt"

echo "[*] Generating the baseline file hashes..."
find "$target_dir" -type f -exec sha256sum {} \; > "$hash_file"
echo "[*] Baseline file hashes generated and saved to $hash_file"

echo "[*] Monitoring for file changes..."
changed=false

while IFS= read -r line; do 
    stored_hash=$(echo "$line" | awk '{print $1}')
    file_path=$(echo "$line" | awk '{print $2}')

    if [ -f "$file_path" ]; then
        current_hash=$(sha256sum "$file_path" | awk '{print $1}')
        if [ "$stored_hash" != "$current_hash" ]; then
            echo "[!] File changed: $file_path"
            echo "Old hash: $stored_hash, New hash: $current_hash"
            changed=true
        fi
    else
        echo "[!] File deleted: $file_path"
        changed=true
    fi
done < "$hash_file"

if ! $changed; then
    echo "[✓] No changes detected in files."
fi