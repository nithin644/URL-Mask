# URLHider

URLHider is a sophisticated command-line tool designed for URL masking and shortening, enabling users to create disguised URLs for various purposes, including cybersecurity testing and research. Built with Python, it leverages popular URL shortening services to generate masked links that can help in understanding and mitigating potential phishing threats.

## Features

- **URL Validation**: Ensures input URLs are properly formatted before processing.
- **Multiple Shorteners**: Supports TinyURL, DAGd, and CLCKRU for URL shortening.
- **Domain Masking**: Allows masking URLs with custom domains and optional phishing keywords.
- **Professional CLI**: Color-coded output for enhanced user experience.
- **Error Handling**: Robust input validation and error messaging.

## Installation

### Prerequisites

- Python 3.6 or higher
- Internet connection for URL shortening services

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/URLHider.git
   cd URLHider
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This will install the required `pyshorteners` library.

3. **Run the Tool**:
   ```bash
   python URLHider.py
   ```

   For information about the tool:
   ```bash
   python URLHider.py about
   ```

## Usage

1. Launch the tool by running `python URLHider.py`.
2. Enter the original URL when prompted (e.g., `https://google.com`).
3. Select a URL shortening service from the options.
4. Provide a domain name for masking (e.g., `google.com`).
5. Optionally, add a phishing keyword.
6. The tool will output the masked URL.

### Example

```
Enter original url[Ex. https://google.com]: https://example.com
1   TinyURL
2   DAGd
3   CLCKRU
Select an option [1-3]: 1
Enter what domain you want to set[Ex. google.com, facebook.com]: fakebank.com
Do you want to enter phising keyword[yes/no]: yes
Enter phishing keyworkd[Ex: free, login]: login
Masked URL::: https://fakebank.com-login@tinyurl.com/abc123
```

## Requirements

- `pyshorteners`: For URL shortening functionality.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Author

Developed by Nithin 3> at IHA089. For more information, visit our cybersecurity solutions page.
