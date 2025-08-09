<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Useless Fans 🎯

## Basic Details
### Team Name: Kudoos


### Team Members
- Team Lead: Anandhu S Nair - CET
- Member 2: Abhinav K P - CET

### Project Description
It finds the speed of fan by giving a video of a rotating fan.

### The Problem (that doesn't exist)
Have you ever laid back in your bed looking at your ceiling and wondered "how fast is my fan spinning?". No? well, we have and that's what motivated us to build this "truely-usefull" project to find the spin with just a video recording from your mobiile. Now with our system, you can find the solution to this revolting question in a matter of seconds.


### The Solution (that nobody asked for)
This project uses computer vision with OpenCV and the Structural Similarity Index (SSIM) to detect when the fan blades return to the same position in a video. By calculating the time between these repeated positions, the program estimates the fan's rotations per minute (RPM) accurately — all from a simple video, without any extra equipment.
TLDR: using maths, logic and python 

## Technical Details
### Technologies/Components Used
For Software:
- Languages:Python
- Frameworks used:None
- Libraries used:
  opencv-python – for video processing
  numpy – for numerical operations
  scikit-image – for SSIM similarity detection
  matplotlib (optional) – for plotting result
- Tools used:VS Code,GitHub

For Hardware:
- Main components: Standard table fan or ceiling fan ,Webcam or smartphone camera
- Specifications: Camera resolution ≥ 720p recommended, FPS ≥ 60
- Tools required: Camera


# Screenshots
<img width="1536" height="898" alt="grid_of_frames_with_high_similarity" src="https://github.com/user-attachments/assets/96ac3fc6-6d59-4afc-9075-407f4ef9a298" />
Of all the frames we separate all of those which shows high similarity with the first frame which evident here

<img width="1400" height="800" alt="similarity_score_of_each_frames" src="https://github.com/user-attachments/assets/a386bf65-af8f-4e5f-95fa-2f4b8470f213" />
We now plot the frames and their corresponding ssmi scores along side, elengantly enough we can witness a standing wave formation!
for math enthusiasts: it is due to the fact that we are dealing with two different frequencies interfering with each other constructively: that of camera (fps)
and that of fan(rpm)

<img width="1920" height="1200" alt="code_in_action" src="https://github.com/user-attachments/assets/b02ce555-bfd0-41d5-a701-b5d8dafab86a" />
sample screenshot of code running in action

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)

#### fin
