import os

# DISASTER
folder_path1 = '/home/yuying/Downloads/test/test_disaster'

file_list1 = os.listdir(folder_path1)

for file_name in file_list1:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path1, file_name), 'r') as txt_file:
            prompts = txt_file.read()
            modified_prompts = f"Photography, Disaster, Incident, Realistic, {prompts}"
        with open(os.path.join(folder_path1, file_name), 'w') as txt_file:
            txt_file.write(modified_prompts)

# ART
folder_path2 = '/home/yuying/Downloads/test/test_art'

file_list2 = os.listdir(folder_path2)

for file_name in file_list2:
    if file_name.endswith('.txt'):
        artist_name_parts = os.path.splitext(file_name)[0].split('_')
        artist_name = ' '.join(artist_name_parts[:-1])
        with open(os.path.join(folder_path2, file_name), 'r') as txt_file:
            prompts = txt_file.read()
            modified_prompts = f"{artist_name}, Art, {prompts}"
        with open(os.path.join(folder_path2, file_name), 'w') as txt_file:
            txt_file.write(modified_prompts)

# NEWS
folder_path3 = '/home/yuying/Downloads/test/test_news'

file_list3 = os.listdir(folder_path3)

for file_name in file_list3:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path3, file_name), 'r') as txt_file:
            prompts = txt_file.read()
            modified_prompts = f"Photography, News, Realistic, {prompts}"
        with open(os.path.join(folder_path3, file_name), 'w') as txt_file:
            txt_file.write(modified_prompts)

# INS
folder_path4 = '/home/yuying/Downloads/test/test_ins'

file_list4 = os.listdir(folder_path4)

for file_name in file_list4:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path4, file_name), 'r') as txt_file:
            prompts = txt_file.read()
            modified_prompts = f"Instagram posts, lifestyle, {prompts}"
        with open(os.path.join(folder_path4, file_name), 'w') as txt_file:
            txt_file.write(modified_prompts)

# PIXIV
folder_path5 = '/home/yuying/Downloads/test/test_pixiv'

file_list5 = os.listdir(folder_path5)

for file_name in file_list5:
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_path5, file_name), 'r') as txt_file:
            prompts = txt_file.read()
            modified_prompts = f"Pixiv style, Anime, {prompts}"
        with open(os.path.join(folder_path5, file_name), 'w') as txt_file:
            txt_file.write(modified_prompts)

