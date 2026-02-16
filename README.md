# 🎉 Year End Event Lucky Draw

## Project Overview
The **Year End Event Lucky Draw** is a web-based application built using Flask that allows users to upload an Excel file containing participant details and randomly selects a winner for a lucky draw. The application is designed to make event management fun and engaging by providing an interactive spinning wheel interface.

---

## Features
- **Upload Excel File**: Upload an Excel file containing participant details.
- **Filter Participants**: Automatically filters participants who have confirmed their attendance.
- **Interactive Spinning Wheel**: Displays a spinning wheel to randomly select a winner.
- **Winner Announcement**: Highlights the winner's name and email with a confetti animation.
- **Responsive Design**: User-friendly interface that works on both desktop and mobile devices.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**:
  - [pandas](https://pandas.pydata.org/): For processing Excel files.
  - [SheetJS](https://sheetjs.com/): For parsing Excel files in the browser.
  - [Particles.js](https://vincentgarreau.com/particles.js/): For background particle effects.
  - [Canvas-Confetti](https://www.kirilv.com/canvas-confetti/): For confetti animations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dheeruthedepl0yer/luckydraw.git
   cd luckydraw
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:80`.

---

## Usage

1. Open the application in your browser.
2. Upload an Excel file containing participant details. The file should have the following columns:
   - **Name**: The participant's full name.
   - **Email**: The participant's email address.
   - **Are you attending the Year End Event?**: Should contain "Yes" for participants who are attending.
3. Click the **Boost Me** button to load the participants.
4. Click the **SPIN** button to start the lucky draw.
5. The winner's name and email will be displayed in the center of the spinning wheel, along with a confetti animation.

---

## File Structure
```
.
├── app.py               # Main Flask application
├── README.md            # Project documentation
├── static/              # Static assets (e.g., CSS, JavaScript, images)
├── templates/           # HTML templates
│   └── index.html       # Main interface for the application
└── text/                # Placeholder for additional text files
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/)
- [SheetJS](https://sheetjs.com/)
- [Particles.js](https://vincentgarreau.com/particles.js/)
- [Canvas-Confetti](https://www.kirilv.com/canvas-confetti/)
