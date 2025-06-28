import os
from PIL import Image
import random
from tqdm import tqdm
import shutil

# Path to the parent folder containing subfolders with images
parent_folder = 'alzheimer_data'

def augment_images(input_image, rotation_degrees):
    augmented_images = []
    img = Image.open(input_image)
    for degree in rotation_degrees:
        rotated_img = img.rotate(degree, expand=True)
        augmented_images.append((degree, rotated_img))
    return augmented_images

pbar = None

for subfolder in os.listdir(parent_folder):
    subfolder_path = os.path.join(parent_folder, subfolder)
    if os.path.isdir(subfolder_path):
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        num_images = len(image_files)
        print(f"Processing subfolder '{subfolder}' - Number of images: {num_images}")

        augmentation_needed = max(3200 - num_images, 0)

        if augmentation_needed > 0:
            output_subfolder = os.path.join(output_folder, subfolder)
            os.makedirs(output_subfolder, exist_ok=True)

            for image_file in image_files:
                input_image_path = os.path.join(subfolder_path, image_file)
                output_image_path = os.path.join(output_subfolder, image_file)
                shutil.copy2(input_image_path, output_image_path)

                remaining_augmentation = 3200 - len(os.listdir(output_subfolder))

                if remaining_augmentation > 0:
                    rotation_degrees = random.sample(range(1, 361), remaining_augmentation)

                    augmented_images = augment_images(output_image_path, rotation_degrees)
                    for degree, rotated_img in augmented_images:
                        new_image_name = f"augmented_{degree}_{image_file}"
                        new_image_path = os.path.join(output_subfolder, new_image_name)
                        rotated_img.save(new_image_path)

                if pbar is None:
                    pbar = tqdm(total=num_images * (remaining_augmentation + 1))

                pbar.update(num_images * (remaining_augmentation + 1))

               
if pbar:
    pbar.close()

print("Augmentation complete.")
