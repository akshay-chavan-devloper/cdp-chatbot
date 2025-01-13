# cdp-chatbot
## Overview
The *Support Agent Chatbot* is a Python-based application designed to assist users in finding answers to common "how-to" questions about four major Customer Data Platforms (CDPs): *Segment, **mParticle, **Lytics, and **Zeotap*. The chatbot extracts information from preloaded documentation files and delivers accurate, step-by-step guidance for tasks and configurations.

---

## Features

### Core Features
1. *"How-to" Question Handling*:
   - Answers questions about tasks within Segment, mParticle, Lytics, and Zeotap.
   - Example: "How do I set up a new source in Segment?"

2. *Documentation Extraction*:
   - Retrieves relevant instructions from text files (segment.txt, mparticle.txt, etc.) based on user queries.

3. *Variation Handling*:
   - Processes diverse phrasings of questions.
   - Filters out irrelevant or unrelated questions.

4. *Cross-CDP Comparisons*:
   - Provides insights into feature differences between the platforms.
   - Example: "How does Segment’s audience creation compare to Lytics’?"

5. *Advanced Support*:
   - Handles queries about complex configurations, advanced integrations, and platform-specific use cases.

6. *Web Interface*:
   - Simple and intuitive web-based interface using Flask.

7. *Modular Design*:
   - Easily extendable to include more CDPs or integrate additional features like NLP.

---

## Technology Stack

- *Backend*: Python, Flask
- *Frontend*: HTML, CSS (via Flask templates)
- *Data*: Preconfigured text files for each CDP (segment.txt, mparticle.txt, etc.)
- *Environment*: Local development setup using Python

---

## Installation and Setup

### Prerequisites
- Python 3.10 or later installed on your system.
- Basic understanding of Python and Flask.

### Steps
1. *Clone the Repository*:
   bash
   git clone <repository_url>
   cd support-agent-chatbot
   

2. *Install Dependencies*:
   bash
   pip install -r requirements.txt
   

3. *Prepare Documentation*:
   - Place the text files (segment.txt, mparticle.txt, lytics.txt, zeotap.txt) in the documentation folder.

4. *Run the Application*:
   bash
   python app.py
   

5. *Access the Chatbot*:
   - Open your browser and navigate to: http://127.0.0.1:5000

---

## Usage
1. Type your question in the chatbot interface (e.g., "How do I create a user profile in mParticle?").
2. The chatbot will fetch relevant instructions from the documentation and display them.
3. For cross-platform comparisons, ask questions like "Compare audience segmentation in Segment and Lytics."

---

## Folder Structure

project-folder/
|-- app.py                  # Main application file
|-- requirements.txt        # Python dependencies
|-- templates/
|   |-- index.html          # Frontend template
|-- documentation/
|   |-- segment.txt         # Documentation for Segment
|   |-- mparticle.txt       # Documentation for mParticle
|   |-- lytics.txt          # Documentation for Lytics
|   |-- zeotap.txt          # Documentation for Zeotap


---

## Future Enhancements
1. *Integrate NLP*: Improve question parsing and response accuracy using natural language processing.
2. *Voice-based Interaction*: Enable voice commands and responses.
3. *Live Deployment*: Deploy the chatbot to a cloud platform (e.g., AWS, Heroku).
4. *Additional CDPs*: Expand support for more platforms.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements
- Official documentation from Segment, mParticle, Lytics, and Zeotap.
- Flask framework for web application development.

---

## Contact
For any questions or feedback, please contact:
- *Name*: Chavan Akshay Ravindra
- *Email*: chavanakshay15072003@gmail.com
- *GitHub*: https://github.com/akshay-chavan-devloper

