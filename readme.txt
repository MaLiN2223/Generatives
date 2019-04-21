===========================================
The QUT FISH Dataset
===========================================

This fish dataset currently consisting of 3,960 images collected from 468 species. This data consists of real-world images of fish captured in conditions defined as "controlled", "out-of-the-water" and "in-situ". The "controlled", images consists of fish specimens, with their fins spread, taken against a constant background with controlled illumination. The "in-situ" images are underwater images of fish in their natural habitat and so there is no control over background or illumination. The "out-of-the-water" images consist of fish specimens, taken out of the water with a varying background and limited control over the illumination conditions. A tight red bounding box is annotated around the fish. Sketch images are not used in this paper.

For more information about the dataset, visit the project website:

https://wiki.qut.edu.au/display/cyphy/Fish+Dataset

If you use the dataset in a publication, please cite the dataset in

@inproceedings{anantharajah2014local,
  title={Local inter-session variability modelling for object classification},
  author={Anantharajah, Kaneswaran and Ge, ZongYuan and McCool, Christopher and Denman, Simon and Fookes, Clinton B and Corke, Peter and Tjondronegoro, Dian W and Sridharan, Sridha},
  booktitle={Winter Conference on Applications of Computer Vision (WACV), 2013 IEEE Conference on},
  year={2014}
}

=========================
Directory Information
=========================

raw images:     fish images with background content
cropped images: fish images with minimum background 

-/annotations: 
We provide manual annotations for each of the raw images, each annotation consists of a bounding box. This bounding box is defined by four pairs of points that consist of a clockwise sequence of points. If the fish is facing to the left of the image then the bounding box annotation sequence consists of the following sequence.

bounding_box: <top_x_left>  <top_y_left> ; <top_x_right>  <top_y_right>; <bottom_x_right> <bottom_y_right>; <bottom_x_left>  <bottom_y_left> 

Otherwise if the fish is facing to the right of the image it consists of the following sequence.

bounding_box:  <top_x_right>  <top_y_right>; <bottom_x_right> <bottom_y_right>; <bottom_x_left>  <bottom_y_left>; <top_x_left>  <top_y_left>; 

An example annotation file for a fish facing to the left would be: 
bounding_box: 4.62129032258 192.955483871; 554.794193548  192.955483871; 554.794193548    29.0741935484;    4.62129032258    29.0741935484 
              
All cropped fish images are facing from right to left. 

-/Images/raw_images: 
original fish images with cropping annotation files.
The images organized in subdirectories based on family and species.

-/Images/cropped: 
fish images cropped.
The images organized in subdirectories based on family and species. 

=========================
IMAGES AND CLASS LABELS:
=========================

The filenames (full image name) are formed using the following method:

<species name>_<imageID>

The imageID is an integer. As an example imageID 4 for "acanthaluteres_brownii" is given by
"acanthaluteres_brownii_4"

------- List of image files with image type and class label and image type (final_all.lst) ------
<species/class number>=<species name>=<image type>=<full image name>

As an example:
18=aluterus_scriptus=insitu=aluterus_scriptus_16
the 18th class is "aluterus_scriptus" and the file "aluterus_scriptus_16" is an image of this class "in-situ".
------------------------------------------

==================================================
Experiment and Evaluation Protocol
==================================================

protocol 1: model enrolled with one controlled and one in-situ image
protocol 1a: enrolled with one controlled image only 
protocol 1b: enrolled with one in-situ image only 

! Only protocol 1a and 1b is presented in the paper which can be found in page 5. !

!!!!!!!
Please note that when enrolling a new class (model/fish species) we do not use information about the other classes in that set. 
You could use the training set as the negative classes if you were training a discriminative classifier. This makes the problem a much more challenging open set problem.
!!!!!!!


------- List of files to train the background model (train_list_<protocol name>.lst) ------
The list of image file names is contained in the file, with each line corresponding to one image:
<species name>_<imageID>
------------------------------------------

------- List of development stage enrolled files (dev_enrol_list_+ <protocol name>.lst) ------
The list of image file names is contained in the file, with each line corresponding to one image:
<species name>_<imageID>
------------------------------------------

------- List of development stage test files (dev_test_list_+ <protocol name>.lst) ------
The list of test image file names is contained in the file, with each line corresponding to one image:
<species name>_<imageID>
------------------------------------------

------- List of evaluation stage enrolled files (eval_enrol_list_+ <protocol name>.lst) ------
The list of image file names is contained in the file, with each line corresponding to one image:
<species name>_<imageID>
------------------------------------------

------- List of development stage test files (eval_test_list_+ <protocol name>.lst) ------
The list of test image file names is contained in the file, with each line corresponding to one image:
<species name>_<imageID>
------------------------------------------

For more details, please refer to the paper.

==================================================
Image copyright
==================================================

All of the images used were obtained from the FishMap website. This images should be used for research purposes only. 
We suggest that you use the following images in papers (and cite the author and copyright information):

//////////////////////////////////////////////////
aphareus_furca_15,Dennis Polack,CC-BY-NC-SA-V3
aphareus_furca_16,Dennis Polack,CC-BY-NC-SA-V3
aphareus_rutilans_5,John E. Randall,CC-BY-NC-V3 
aphareus_rutilans_6,Dennis Polack,CC-BY-NC-SA-V3 
achoerodus_gouldii_3,G. Edgar,CC BY-NC Attribution-Non-Commercial 3.0 Australia
achoerodus_gouldii_2,Vicki Billings,CC-BY-NC-SA
aethaloperca_rogaa_1,I Shaw,Australian National Fish Collection, CSIRO
aethaloperca_rogaa_2,I Shaw,CC-BY
achoerodus_viridis_1,Australian National Fish Collection CSIRO,CC Attribution-Non Commercial 3.0
achoerodus_viridis_2,MESA,CC-BY (Creative Commons Attribution)
//////////////////////////////////////////////////

We suggest that if you reproduce images for papers that you check the copyright for the relevant image (we have maintained a list which can be found in "Licence & Authors - Sheet.pdf"). If unsure, then please don't use this image.

==================================================
Updated: folder pre_set experiment with numbers
==================================================
We made a new folder contains all cropped images named with number. This system is easier
to use if you are using matlab.

database_1a.mat: mat file with images used for protocol 1a and class label
database_1b.mat: mat file with images used for protocol 1b and class label
p1a_train: images used for enrol in protocol 1a
p1b_train: images used for enrol in protocol 1b
p1a_test: images used for test in protocol 1a
p1b_test: images used for test in protocol 1b


