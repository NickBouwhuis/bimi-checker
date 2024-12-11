# BIMI Record Checker

A web-based tool for checking BIMI (Brand Indicators for Message Identification) DNS records across multiple domains. This application helps email administrators and brand managers verify their BIMI implementation by checking DNS records and validating SVG logos.

## Features

- Bulk domain checking for BIMI records
- Real-time SVG logo validation
- Visual progress tracking for bulk checks
- Statistical overview of results
- SVG logo preview
- Filterable results view
- Responsive web interface

## Requirements

- Python 3.x
- Flask
- dnspython
- requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nickbouwhuis/bimi-check.git
cd bimi-check
```

2. Setup a venv and install the required dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter one or more domains (one per line) in the text area

4. Click "Check BIMI Records" to start the verification process

## How It Works

The application performs the following checks for each domain:

1. Looks up the BIMI DNS record (`default._bimi.domain.com`)
2. Parses the BIMI record to extract the SVG logo URL
3. Validates the SVG logo by:
   - Checking if the URL is accessible
   - Verifying the content type is `image/svg+xml`
4. Displays results with:
   - Domain name
   - BIMI record content
   - SVG logo preview (if valid)
   - Success/failure status

## Features in Detail

### Real-time Progress Tracking
- Progress bar showing completion status
- Domain processing counter
- Percentage completion indicator

### Statistics Dashboard
- Total domains processed
- Number of BIMI records found
- Number of domains without BIMI
- Success rate calculation

### Result Filtering
- Option to hide domains without BIMI records
- Instant filtering without reloading

### Visual Feedback
- SVG logo previews
- Clear success/failure indicators
- Formatted record display

## Technical Details

- Built with Flask (Python web framework)
- Uses `dnspython` for DNS record lookups
- Implements asynchronous domain checking
- Processes domains in batches for optimal performance
- Client-side rendering for responsive user experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.