import os

source_folder = 'C:/Users/Windows 10/Downloads/test-file/test_ile/'
output_folder = 'C:/Users/Windows 10/Downloads/test-file/File103/'

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            # Cek apakah '103' ada di dalam konten
            if ' 103 ' in content:
                with open(os.path.join(output_folder, filename), 'w') as output_file:
                    output_file.write(content)

print(f'Hasil sortir telah disimpan di folder: {output_folder}')