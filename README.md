# 👋🏼Sign Language Detection Project

Welcome to the Sign Language Detection project! This project aims to detect and interpret sign language gestures using deep learning techniques.

## Installation

To get started with the Sign Language Detection project, follow these steps:

1.  **Clone the Repository:**
       
    `git clone https://github.com/yourusername/sign-language-detection.git`
    
     `cd sign-language-detection`
    
2.  **Install Anaconda:** If you haven't already installed Anaconda, download and install it from the official website.
    
3.  **Create and Activate the Environment:**
  
    `conda env create -f environment.yml`
    
    `conda activate sign-language-env` 
    
    This will create a new Anaconda environment named `sign-language-env` and activate it.
    
5.  **Install Required Libraries:**

    `pip install -r requirements.txt` 
    
    This will install all the necessary Python libraries required for the project.
    

## Running the Project

Once you've set up the environment and installed the dependencies, follow these steps to run the Sign Language Detection project:

1.  **Locate the Project Directory:** Navigate to the project directory in your command-line interface.
    
2.  **Activate the Environment:**

    `conda activate sign-language-env` 
    
3.  **Run the Detection Script:**

    `python yolov5/detect.py --weights yolov5/runs/train/exp4/weights/last.pt --source 0` 
    
    This command runs the detection script, using the trained weights from the specified directory.
    

## Example Usage

Here's an example command for running the detection script:\

`python yolov5/detect.py --weights yolov5/runs/train/exp4/weights/last.pt --source 0` 

This command detects sign language gestures using the YOLOv5 model with the specified weights.
