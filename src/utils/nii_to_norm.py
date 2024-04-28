import os
import nibabel as nib
import numpy as np


def normalize_nifti(folder_path):
    normalized_files_seg = []
    normalized_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".nii.gz") and "warpcoef" not in file:  # Assuming NIfTI files are in gzip format
                file_path = os.path.join(root, file)

                # Read NIfTI file
                nifti_image = nib.load(file_path)
                nifti_data = nifti_image.get_fdata()

                # Normalize the values to the range of 0 to 255
                nifti_norm = (nifti_data - nifti_data.min()) / (nifti_data.max() - nifti_data.min()) * 255
                # nifti_norm = nifti_norm.astype('uint8')

                # Create a new NIfTI image with the normalized data
                normalized_nifti = nib.Nifti1Image(np.flip(nifti_norm.transpose([2, 1, 0])), nifti_image.affine, nifti_image.header)

                output_file = os.path.join(root, file[:-7]) + "_norm.nii.gz"
                nib.save(normalized_nifti, output_file)

                normalized_files.append(output_file)
                normalized_files_seg.append(os.path.join(root, file[:-7]) + "_norm_seg.nii.gz")

    # Create a text file with the paths to the normalized files
    txt_file = os.path.join(folder_path, "normalized_files.txt")
    with open(txt_file, 'w') as f:
        f.write('\n'.join(normalized_files))

    txt_file = os.path.join(folder_path, "normalized_files_seg.txt")
    with open(txt_file, 'w') as f:
        f.write('\n'.join(normalized_files_seg))


if __name__ == "__main__":
    folder_paths = [
        # "/home/ai2lab/datasets/roberto/Reference/",
        "/home/ai2lab/datasets/roberto/PS-reg/10x/",
        # "/home/ai2lab/datasets/roberto/Non-enhanced/10x/",
        # "/home/ai2lab/datasets/roberto/Norm-baseline-nifti-reorient/"
    ]

    for folder_path in folder_paths:
        normalize_nifti(folder_path)

    # Process the text file
    with open('/home/ai2lab/datasets/roberto/test.txt') as f:
        lines = f.readlines()

    # Process the lines as needed
    # ...

    print('NIfTI files normalized and saved successfully!')