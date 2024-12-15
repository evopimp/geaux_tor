# Geaux Tor

## Project Overview
Geaux Tor is a Python-based application designed to connect to the Tor network for anonymous browsing and to enable the scraping of image and document files from the web. This project focuses on privacy, efficiency, and usability.

---

## Features
- **Tor Network Integration**: Browse anonymously through the Tor network.
- **Image Scraping**: Collect image files (e.g., `.jpg`, `.png`) from specified URLs.
- **Document Scraping**: Collect document files (e.g., `.pdf`, `.docx`) from specified URLs.
- **File Storage**: Automatically store scraped files in a user-defined folder.

---

## Milestones

### Milestone 1: Setup and Initial Configuration
- Install Python packages: `requests`, `beautifulsoup4`, `stem`, `pytor`.
- Configure the application to connect to the Tor network.
- Verify the connection to the Tor network.

### Milestone 2: Basic Web Scraping
- Create an `ImageScraper` class to scrape images from a given URL.
- Create a `DocumentScraper` class to scrape documents from a given URL.

### Milestone 3: Integration and Testing
- Integrate `ImageScraper` and `DocumentScraper` into the main application.
- Test scraping functionality for both images and documents.
- Implement robust error handling and logging mechanisms.

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd geaux_tor
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the main script:
   ```bash
   python src/main.py
   ```
2. Enter the URL for scraping images or documents when prompted.
3. Access the scraped files in the specified storage folder.

---

## Contributing
Contributions are welcome! To get started:

1. Fork the repository and create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message here"
   ```
3. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Open a pull request and describe your changes.

For bug reports or feature requests, please open an issue.

---

## File Structure
```
geaux_tor/
├── src/
│   ├── main.py       # Main application entry point
│   ├── scraper.py    # Scraping classes and logic
│   └── utils.py      # Utility functions
├── data/             # Folder for storing scraped files
├── tests/            # Unit tests
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contact
For any questions or suggestions, please contact the project maintainer:
- **Name**: "Daniel"
- **Email**: dhopkins@geauxspecialist.com
