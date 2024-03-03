with open("preproinsulin-seq.txt", "r") as input_file:
    content = input_file.readlines();
print(content);
remaining_lines = content[1:-1];
print(remaining_lines);
processed_lines = [];
for line in remaining_lines:
    line = line.replace(' ', '');
    line = line.replace('\n', '');
    processed_lines.append(line.lstrip('0123456789'));
print(processed_lines); 
with open("preproinsulin-seq-clean.txt", 'w') as output_file:
    output_file.writelines(processed_lines);
lowercase_count = 0
with open("preproinsulin-seq-clean.txt", 'r') as file:
   content = file.read();
   for char in processed_lines:
    if(char.islower()):
        lowercase_count += 1;
# Cleaning the content
cleaned_content = ''.join(filter(str.isalpha, content))

# Save the cleaned content to preproinsulin-seq-clean.txt
with open("preproinsulin-seq-clean.txt", "w") as clean_file:
    clean_file.write(cleaned_content)

# Confirm that the file has 110 characters
if len(cleaned_content) == 110:
    print("File has 110 characters.")
else:
    print("File does not have 110 characters.")

# Extract amino acids 1-24 to lsinsulin-seq-clean.txt
ls_insulin = cleaned_content[:24]
with open("lsinsulin-seq-clean.txt", "w") as ls_file:
    ls_file.write(ls_insulin)

# Verify that the file has 24 characters
if len(ls_insulin) == 24:
    print("lsinsulin-seq-clean.txt has 24 characters.")
else:
    print("lsinsulin-seq-clean.txt does not have 24 characters.")

# Extract amino acids 25-54 to binsulin-seq-clean.txt
bin_insulin = cleaned_content[24:54]
with open("binsulin-seq-clean.txt", "w") as bin_file:
    bin_file.write(bin_insulin)

# Verify that the file has 30 characters
if len(bin_insulin) == 30:
    print("binsulin-seq-clean.txt has 30 characters.")
else:
    print("binsulin-seq-clean.txt does not have 30 characters.")

# Extract amino acids 55-89 to cinsulin-seq-clean.txt
c_insulin = cleaned_content[54:89]
with open("cinsulin-seq-clean.txt", "w") as c_file:
    c_file.write(c_insulin)

# Verify that the file has 35 characters
if len(c_insulin) == 35:
    print("cinsulin-seq-clean.txt has 35 characters.")
else:
    print("cinsulin-seq-clean.txt does not have 35 characters.")

# Extract amino acids 90-110 to ainsulin-seq-clean.txt
a_insulin = cleaned_content[89:110]
with open("ainsulin-seq-clean.txt", "w") as a_file:
    a_file.write(a_insulin)

# Verify that the file has 21 characters
if len(a_insulin) == 21:
    print("ainsulin-seq-clean.txt has 21 characters.")
else:
    print("ainsulin-seq-clean.txt does not have 21 characters.")