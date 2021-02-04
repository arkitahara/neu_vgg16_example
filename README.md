# neu_vgg16_example
Tutorial to use pre-trained VGG16 for defect classification on NEU Surface Defect Database. This is intended for demonstration purposes at Carnegie Mellon University Department of Materials Science and Engineering. 

## Setting up the environment
The environment file `mse_env.yml` is included in this repository. Use this to build a stable virtual environment to run this code. If you need help setting this up, [read the docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

## Project Structure
The main directory `neu_vgg16_example` should have the following contents:
- data
- notebooks
- results
- src
- mse_env.yml
- README.md

## Data
Images for this example were pulled from K. Song and Y. Yan [1]. The data are not included in this repository. Please use the original author's source below to fetch the data.


[1] K. Song and Y. Yan, “A noise robust method based on completed local binary patterns for hot-rolled steel strip surface defects,” Applied Surface Science, vol. 285, pp. 858-864, Nov. 2013.(paper)

http://faculty.neu.edu.cn/yunhyan/NEU_surface_defect_database.html

## Notebooks
This is where all iPython notebooks will be kept. Notebooks are great for quickly trying out new ideas. This is also where the main narrative of this tutorial resides.

## Results
This is where all exported figures will be stored.

## SRC
This is the *source code* directory. All helper functions will be (hopefully) neatly stored here.
