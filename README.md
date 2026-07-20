# Plant Growth Tracker using OpenCV

An automated computer vision script that uses HSV thresholding and contour analysis to calculate the pixel height of a growing plant over a multi-day timelapse.

## How It Works
* **Color Masking:** Converts the BGR image to the HSV color space to cleanly isolate the green plant from the background and soil.
* **Contour Analysis:** Targets the largest detected green object to filter out minor noise or leaf breaks.
* **Measurement:** Calculates a bounding box around the sprout and draws indicators tracking its height in pixels.

## Visual Output
### Day 5: Early Sprout Detection
<img width="1366" height="768" alt="Day5" src="https://github.com/user-attachments/assets/5bfa2358-70a2-418c-9a67-f5b61b6f291e" />


### Day 12: Full Growth Tracking

<img width="1366" height="768" alt="Day12" src="https://github.com/user-attachments/assets/ed56b5aa-1513-4965-8612-ca9a2969e5e3" />

## How to Run This Project

If you want to test this script on your own machine, follow these steps:

### Option 1: Using the Provided Samples
1. Download the images from the `Samples` folder in this repository and change the locations appropriate.
2. Update the `imread` file path in the script to match where you saved them on your computer.
3. Run the script and press any key to loop through the daily images.

### Option 2: Using Your Own Images
If you want to track a completely different plant or object, you will need to tweak a few settings in the code:
* **Image Directory:** Change the path inside `cv2.imread()` to point to your image folder.
* **Loop Range:** Modify the `for i in range(start, end):` numbers to match the total number of images you have.
* **Color Limits:** If your plant has a different shade of green (or if you are tracking a non-green object), adjust the HSV threshold variables:
  ```python
  l_lim = (H_min, S_min, V_min)
  u_lim = (H_max, S_max, V_max)
