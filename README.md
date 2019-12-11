# EC601 Final Project: Coded Aperture Imaging System
<p align="middle"><img src="https://github.com/mbu54/601project/blob/master/Coded_aperture_mask_(for_gamma_camera).jpg" align="middle" style="width:300px;height:300px;"></p>
 
## Product Mission
Our goal is to develop a program that runs a coded aperture mask through various simulated optical tests and outputs the results of these tests to help the user determine in which applications the mask would perform optimally. Additionally, these results will be saved to a simple database that allows the user to search through. Time permitting, we will build a physical setup for the coded aperture system, and extra time permitting we would like to build an entire system of which our coded aperture would be just one part (e.g. camera or telescope). 

  ### User Stories (for coded aperture applications)
  - I, the astronomer, want to be able to view images with a lensless telescope.
  - I, the physician, want to be able to perform x-ray scans without lenses.
  - I, the photographer, want to be able to take low light lensless pictures.
  - I, the photographer, want to be able to take pictures without the glare effect from a lens.
  - I, the scientist, want to be able to capture images without the use of a lens.
  - I, the scientist, want to be able to take microscopic images in a space where a lens cannot fit.
  - I, the astronaut, want to be able to capture images in space without a lens.
  - I, the researcher, want a developed aperture that is adaptable to use in my imaging device.
  - I, the developer, want an adaptable coded aperture to save time developing my own product.
  
  ### User Stories (for analysis program)
  - I, the scientist/researcher/student, want to be able to test my coded aperture in various optical simulations.
  - I, the scientist/researcher/student, want to have a database to search what kind of coded aperture works best in a given      application.

  ### Customers

  Our target audeiences are photographers and researchers involved in lensless imaging.

  ### Minimum Value Product (MVP)

  MVP: Design a simulation program that runs a coded aperture mask through various optical tests and stores the data in searchable format.

## Product Analysis

  ### Competitors (for coded aperture masks and applications)
  - UT-Battelle LLC (CA Imaging System): can image on the order of microns
  - Qinetiq Ltd (CA Imaging System): allows imaging of different fields of view, coded mask is reconfigurable
  - Huang et. al. (CA X-Ray Imaging System): can analyze enveloped material, limited to x-ray
  
  ### Competitors (for analysis program/database)
  - Some PhD theses have discussed the issue and provided individual case studies
  - Currently no existing database
  
  ### Technology
  - Store data on googlesheets using API (maybe TinyDB)
    - relatively small amounts of data
    - easily searchable
    - easily accessible
  - Use python as programming languague
    - open source language that anyone can use to run our open source code (as oppose to Matlab)
    - lots of math libraries (numpy, scipy) for image processng
  - Using Flask to develop the site for inputting data
    - prevents users from adjusting the code, ruining data, etc.
    - should be more user-friendly
  - Hosting our site with Heroku
  
  ### Issues to consider
   - Masks that allow different amounts of light
   - Different sized masks
   - How we want to normalize the output of our tests
   - What type of input file(s) is/are allowed
   - Be aware of limitations of our optical tests
   - Keep analysis code opensource so others can modify the optical tests to fit their needs
   
  ### Database Notes
  We will not be focusing on the development of a database system in part due to time restraints as well as because a complex database is not necessary for what we want it to do (listed below).
   - Public use (open source)
   - Searchable
   - Low memory intensive
  
## System Design
![system diagram](https://github.com/mbu54/601project/blob/master/Screen%20Shot%202019-10-07%20at%208.48.14%20PM.png)

 ### Mathematical concept
 - An image is resolved through the convolution and deconvolution of an object sending rays of light through the coded aperture
   - The object is called the Point Source (x,y), a two-dimensional figure which is converted to a digital signal
   - The coded aperture is represented as an impulse response function, or Point Spread Function (PSF)
 - Both the point source and PSF are convolved together to create the signal of image that is seen through the coded aperture
 - To see the final image, the image signal is deconvolved, leaving behind a time-domain representation of the object
 
 ### Concerns
 - While the far-field test is fairly straight-forward, the near-field test has the difficulty of dealing with angled rays instead of using paraxial approximations, making the approach to applying the near-field test more challenging than we first imagined.
 - We realized in our analysis of the far-field test that without the inclusion of background noise, our analysis of the apertures may not be as effective as can be. We will be using part of sprint 3 to look at how to include noise without getting too overwhelmed.
 
 ### New Approaches
 - Instead of making a 'near-field' test and engaging with the deformities that come from analyzing on a scale relative to the wavelength, we adapt a 'mid-field' test, which can still be on a microscopic scale relatively, but still be on a scale much larger than the wavelength of the input light.
 - We have changed from using Wix as out site host to developing a basic site with Python's Flask library and implementing it live via Heroku.

## Demos

 ### Far-Field Testing with a Randomly Generated CA
 <p align="middle"><img src="https://github.com/mbu54/601project/blob/master/Aperture_Tests/farfielddemo.png"></p>
 
 ### Mid-Field Testing with a Randomly Generated CA
 
## User Guide

 ### What you will need:
 - A coded aperture saved as a .npy file
   - Size of the aperture should be 100x100 pixels
 - Access to site link (coming soon)
 
 ### Steps
 1. Head to our website, input your information, and upload your aperture file
 2. Our program will analyze the aperture in the mid and far-field, then calculate its error with respect to the original image
 3. The program will return the error, smaller values indicating a more accurate aperture
 4. The program will also give you a link to access our drive containing all pervious apertures and the scores for each one
 
## Links and References

<a href="https://drive.google.com/drive/folders/1znG365a-_0aR97n4F3Bvw1yOBPKbYH1N?usp=sharing">Sprint Presentations</a>

## Notes and Updates
- 10/13/19: Finished Goggle Sheets API assembly
- 10/27/19: Added to system design section; added folder for aperture tests
- 10/29/19: Finished pinhole control test; finalizing far-field test
- 11/2/19: Added comparison module for original versus reconstructed image; finalized far-field test
- 11/3/19: Included images for far-field test in repo
- 11/4/19: Set up "Main" folder for one-stop access to utilize code
- 11/11/19: Currently working on formalizing the near-field test; needs understanding to set up wave propagation equation
- 11/19/19: Changing near-field test to 'mid-field' test, making approximations for the wavelength of the input light
- 11/20/19: Updated Apeture Tests to include mid-field test
- 12/2/19: Finalized inclusion of noise for both tests, revamped method of site design (Flask)
- 12/4/19: Finishing up assembly of website, figured out how to upload files, parts are all linked on back end
- 12/10/19: Finished integration of front end and back end
