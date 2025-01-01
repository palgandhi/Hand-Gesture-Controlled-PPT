Gesture-Controlled Presentation System

An innovative system that allows users to control slide presentations using hand gestures, eliminating the need for physical clickers or keyboards.

Table of Contents
	1.	Inspiration
	2.	Features
	3.	Technologies Used
	4.	How It Works
	5.	Installation
	6.	Usage
	7.	Future Enhancements
	8.	Demo Video
	9.	Contributing
	10.	License

Inspiration

While giving multiple presentations during my last semester, I found myself constantly distracted by having to manually change slides. This sparked the idea of creating a touch-free, gesture-controlled system to enhance presentation flow and engagement.

Features
	•	Navigate slides by swiping your hand left or right.
	•	Touch-free interaction using a standard webcam.
	•	Lightweight and easy-to-use interface.

Technologies Used
	•	Python: Core programming language.
	•	OpenCV: For capturing and processing video frames.
	•	MediaPipe: For real-time hand tracking and gesture recognition.
	•	PyAutoGUI: To simulate keyboard actions for slide navigation.

How It Works
	1.	The webcam captures video input.
	2.	MediaPipe detects and tracks hand landmarks in real-time.
	3.	Hand gestures (e.g., swipe left or swipe right) are recognized.
	4.	PyAutoGUI triggers the corresponding keyboard event to navigate slides.

Installation
	1.	Clone the Repository

git clone https://github.com/yourusername/gesture-controlled-presentation.git
cd gesture-controlled-presentation  


	2.	Install Dependencies
Ensure Python is installed on your system. Then, install the required libraries:

pip install opencv-python mediapipe pyautogui  


	3.	Run the Script

python main.py  

Usage
	1.	Connect a webcam to your computer.
	2.	Run the script (python main.py).
	3.	Perform the following gestures:
	•	Swipe Right: Move to the next slide.
	•	Swipe Left: Go back to the previous slide.
	4.	Open your presentation software (e.g., PowerPoint) and start presenting!

Future Enhancements
	•	Add gesture-based actions to pause/resume the presentation.
	•	Improve gesture detection accuracy using custom-trained models.
	•	Create a standalone desktop application for easier use.


Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

