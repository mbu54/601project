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
  
  ### Issues to consider
   - masks that allow different amounts of 
   - different sized masks
   - how we want to normalize the output of our tests
   - what type of input file(s) is/are allowed
   - be aware of limitations of our optical tests
   - keep analysis code opensource so others can modify the optical tests to fit their needs
   
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

## Demos

 ### Far-Field Testing with a Randomly Generated CA
 <img src="https://github.com/mbu54/601project/blob/master/Aperture_Tests/originalimage.png" alt="sometext" />
 <p align="middle">Original image, Image reconstructed using a pinhole, Image reconstructed using a CA</p>

## Notes and Updates
- 10/13/19: Finished Goggle Sheets API assembly
- 10/27/19: Added to system design section, added folder for aperture tests
- 10/29/19: Finished pinhole control test; finalizing far-field test
- 11/2/19: Added comparison module for original versus reconstructed image
