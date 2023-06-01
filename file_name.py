import os

def find_files_with_extension(directory, extension):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(file)
    return file_list

def write_file_list_to_txt(file_list, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for file_name in file_list:
            file.write(file_name + "\n")
    print("Dosya listesi başarıyla oluşturuldu.")

# Ana dizin ve uzantıyı belirleyin
directory = r"D:\Onur\e-kitap"  # r ön ekini kullanarak kaçış dizilerini yok sayın
extension = ".epub"

# Dosya listesini bul
file_list = find_files_with_extension(directory, extension)

# Dosya adlarını metin dosyasına yaz
output_file = "dosya_listesi.txt"  # Buraya oluşturulacak metin dosyasının adını belirtin
write_file_list_to_txt(file_list, output_file)
