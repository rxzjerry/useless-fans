from skimage.metrics import structural_similarity as ssim
from scipy.signal import find_peaks
import cv2
import numpy as np
import matplotlib.pyplot as plt


set_new=True
big=[] # to store all the frames in video
score_arr=[] # to store the ssim scores of all frames in relation to frame no.1

cap=cv2.VideoCapture('ref.mp4') # 208 frames total

while (cap.isOpened()):
    ret, frame = cap.read() # frame is an np.ndarray of shape (380, 540, 3)
    if not ret:
        break
    frame=cv2.resize(frame, (540, 380), fx=0, fy=0)
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # change images to grayscale for easier ssim check
    big.append(gray_frame)

    if set_new:
        key=gray_frame # all similarity checking will be done with key, i.e, the first frame
        set_new=False

    score, _= ssim(key,gray_frame, full=True,data_range=255) # check key with current frame (gray_frame)
    score*=100
    score_arr.append(score)
    # print(score)

    # prev=gray_frame
    cv2.imshow('Frame', gray_frame)

    if cv2.waitKey(25) & 0xff==ord('q'):
        break



# if we plot the ssim scores of each frame, we get a line plot (which is displayed later)
# which contains 'peaks' which corresponds to high correlation, which is what we are after
peaks,_=find_peaks(score_arr,distance=2.75)
peaks=peaks.tolist()
peaks.insert(0,0) # auto-add first frame

bigg=np.array(big) # everything needs to be np.array for faster computation
wanted=bigg[peaks]

score_arrn=np.array(score_arr)

rpm_long=[] # equals to no. of peaks
prev_p=0;
fps=0
for p in peaks:
    interval=p-prev_p # frame-difference between succesive peaks
    if interval>0:
        fps=1200/interval # math formula which is dependant on fps (60 here) and some basic math, abstracted for simplicity :)
    rpm_long.append(fps) # fps for 2nd frame onwards
    prev_p=p


# find average rpm over each interval for second
rpm_short=[] # equals to no. of seconds in input video
i=0 
rpm_long=np.array(rpm_long)

bin_size = 60
max_value = rpm_long.max()

# python magic
peaks=np.array(peaks)
for start in range(1, int(max_value) + 1, bin_size):
    end = start + bin_size - 1
    indices = np.where((peaks >= start) & (peaks <= end))[0]
    
    if len(indices) > 0: # Only if there are numbers in this range
        avg_rpm = np.mean(rpm_long[indices])
        rpm_short.append(avg_rpm)


# display the end results:
for i in range(len(rpm_short)):
    print("avg rpm in {}th second: ".format(i+1),end="")
    print(f"{rpm_short[i]:.2f}")

# display cool graphs
# display all the images (frames) which shows high similarity with first frame, as you can see yourself
fig, axes= plt.subplots(6, 10, figsize=(19.2,12))
for i, ax in enumerate(axes.flat):
    if i <len(wanted):
        ax.imshow(wanted[i], cmap="gray")
        ax.set_title("frame no:"+f'{peaks[i]}')

plt.tight_layout()
plt.show()


# graph no.2; here we plot the similarity score of each frame and we can see the peaks we mentioned earlier
# we can notice some mathematical elegance in action
# since we are dealing with two different frequencies i.e, fps of camera and rpm of fan acting together, we can witness 
# a nice 'standing wave' stucture

plt.figure(figsize=(14,8))
plt.plot(np.arange(len(score_arr)), score_arr)
plt.scatter(peaks,score_arrn[peaks],)
plt.xlabel('frame no.')
plt.ylabel('pixel matching score')

plt.show()

cap.release()
cv2.destroyAllWindows()

# also note that eventhough the video we used is 3s long, it is slowed down in the demo video 
# fin
