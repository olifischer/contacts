# Contact Management System

A simple, modern web application for managing contacts with a beautiful user interface. The application allows users to store and view contact information (first name, last name, and email) in a clean, responsive design.

![Contact Form Preview](https://via.placeholder.com/600x400?text=Contact+Form+Preview)

## Features

- 🎨 Modern, responsive UI with gradient background
- 📝 Simple contact form with validation
- 📊 Sticky table headers for better navigation
- 💾 Local storage of contacts in a text file
- 🔄 Real-time updates when adding contacts
- 📱 Mobile-friendly design

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7 or higher installed on your system
* A modern web browser (Chrome, Firefox, Safari, or Edge)
* Basic knowledge of using terminal/command prompt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/contacts.git
cd contacts
```

2. (Optional) Create and activate a virtual environment:
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python3 server.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

3. You can now:
   - Add new contacts using the form
   - View all saved contacts by clicking the "View Contacts" button
   - Scroll through contacts while maintaining a fixed header

## File Structure

```
contacts/
├── README.md
├── requirements.txt
├── server.py
├── index.html
└── contact.txt (created automatically)
```

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript
- **Backend**: Python HTTP Server
- **Storage**: Local text file (contact.txt)
- **Data Format**: CSV (comma-separated values)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/contacts](https://github.com/yourusername/contacts)

## Acknowledgments

- Inspired by modern web design principles
- Built with simplicity and user experience in mind
- Created as a demonstration of full-stack web development 