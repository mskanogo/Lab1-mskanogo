#!/bin/bash

# Purpose: Archive CSV files with timestamps and log all actions

# Define constants
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

echo "=========================================="
echo "CSV File Organizer"
echo "=========================================="
echo ""

# Step 1: Check if archive directory exists, create if it doesn't
if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "Creating archive directory..."
    mkdir "$ARCHIVE_DIR"
    echo "Archive directory created."
else
    echo "Archive directory already exists."
fi

echo ""

# Step 2: Find all CSV files in the current directory
# Use an array to handle filenames with spaces
csv_files=(*.csv)

# Check if any CSV files exist
if [ ! -e "${csv_files[0]}" ]; then
    echo "No CSV files found in the current directory."
    echo "Nothing to archive."
    exit 0
fi

echo "Found ${#csv_files[@]} CSV file(s) to archive."
echo ""

# Step 3: Loop through each CSV file
for csv_file in "${csv_files[@]}"; do
    # Skip if it's not a file (safety check)
    if [ ! -f "$csv_file" ]; then
        continue
    fi
    
    echo "Processing: $csv_file"
    
    # Generate timestamp in format YYYYMMDD-HHMMSS
    timestamp=$(date +"%Y%m%d-%H%M%S")
    
    # Extract filename without extension and the extension
    filename="${csv_file%.csv}"
    extension="csv"
    
    # Create new filename with timestamp
    new_filename="${filename}-${timestamp}.${extension}"
    
    # Define the full path for the archived file
    archived_file="${ARCHIVE_DIR}/${new_filename}"
    
    # Log the action to organizer.log
    echo "=========================================="  >> "$LOG_FILE"
    echo "Archive Action - $(date '+%Y-%m-%d %H:%M:%S')" >> "$LOG_FILE"
    echo "=========================================="  >> "$LOG_FILE"
    echo "Original File: $csv_file" >> "$LOG_FILE"
    echo "New Location: $archived_file" >> "$LOG_FILE"
    echo "Timestamp: $timestamp" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    echo "File Contents:" >> "$LOG_FILE"
    echo "------------------------------------------" >> "$LOG_FILE"
    cat "$csv_file" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    echo "------------------------------------------" >> "$LOG_FILE"
    echo "Archive completed successfully." >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    
    # Move and rename the file to the archive directory
    mv "$csv_file" "$archived_file"
    
    echo " Archived as: $new_filename"
    echo " Logged to: $LOG_FILE"
    echo ""
done

echo "=========================================="
echo "Archival process completed!"
echo "Total files archived: ${#csv_files[@]}"
echo "=========================================="