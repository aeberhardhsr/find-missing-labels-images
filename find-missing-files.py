import glob, os

# only for testing
#os.chdir("test-data")

# change this to the desired direction
os.chdir(r"O:\01_Image_Datasets\BA\05_labeled_dataset")

image_names = []
label_names = []

for file in glob.glob("*.txt"):
    label_names.append((os.path.splitext(file))[0])


for file in glob.glob("*.jpg"):
    image_names.append((os.path.splitext(file))[0])
    

if len(set(image_names) - set(label_names)) == 0:
    print("There are no images without labels")
else:
    print("Image {} has no label".format(set(image_names) - set(label_names)))


#find_images_without_labels = set(image_names) - set(label_names)

if len(set(label_names) - set(image_names)) == 0:
    print("There are no labels without images")
else:
    print("Label {} has no image".format(set(label_names) - set(image_names)))

