import cv2
import random
import IPython.display
from PIL import Image
import numpy as np
import os

DISPLAY_FRAMES_IPYNB = False
SAVE_FRAMES = True



class Videos:
    def __init__(self, directory):
        self.directory = directory
        self.all_files = self.get_all_files(directory)
        self.video_list = [Video(file) for file in self.all_files]
        self.total_frames = sum(video.frame_count for video in self.video_list)

    def get_all_files(self, directory):
        files_list = []
        for root, _, files in os.walk(directory):
            for file in files:
                files_list.append(os.path.join(root, file))
        return files_list

    def print(self):
        print("files in the directory: ", self.directory)
        print("number of files: ", len(self.all_files))
        print("total frame count: ", self.total_frames)

    def get_random_frames(self, n):
        for i in range(n):
            #print("test",i)
            frame = random.randint(1,self.total_frames)
            print(frame)
            for j in range(len(self.video_list)):
                if frame < self.video_list[j].frame_count:
                    print("video: ",self.video_list[j].video_path)
                    print("video frame: ",frame)
                    if (DISPLAY_FRAMES_IPYNB):
                        self.video_list[j].display_frame(frame)
                    if (SAVE_FRAMES):
                        self.video_list[j].get_frame(frame, f"frames/{frame}.PNG")
                        

                    break
                else:
                    frame = frame - self.video_list[j].frame_count
                

class Video:
    def __init__(self, video_path):
        self.video_path = video_path
        self.frame_count = self.get_frame_count(video_path)

    def get_frame_count(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()
        return frame_count

    def get_frame(self, frame_number, output_path=None):
        cap = cv2.VideoCapture(self.video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        success, frame = cap.read()
        cap.release()

        if success:
            if output_path:
                cv2.imwrite(output_path, frame)  # Save as PNG
                print(f"Frame {frame_number} saved as {output_path}")
            return frame
        else:
            print("Error: Could not extract frame.")
            return None

    def display_frame(self, frame_number):
        cap = cv2.VideoCapture(self.video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # Jump to frame

        success, frame = cap.read()
        cap.release()

        if success:
            # Convert BGR (OpenCV) to RGB (PIL)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)

            # Display in Jupyter
            IPython.display.display(img)
        else:
            print("Error: Could not extract frame.")

    def print(self):
        print("video path: ", self.video_path)
        print("frame count: ", self.frame_count)
    
if __name__ == "__main__":
    test = Videos("Videos")
    test.print()
    test.video_list[0].print()
    print("###############################")
    test.get_random_frames(2)