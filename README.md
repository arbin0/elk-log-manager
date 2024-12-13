# Log Message Extractor and Email Notifier

## Overview
This Python script extracts log messages from Elasticsearch via Kibana and sends them to specified email recipients. It automates the process of gathering application logs and sending detailed reports through email.

## Features
- Connects to Elasticsearch via Kibana to retrieve log messages.
- Extracts and formats error messages into JSON format.
- Sends an email with the extracted logs attached as files.

## Requirements

### Python Libraries
- `json`
- `objectpath`
- `requests`
- `smtplib`
- `email`

Install required packages using:
```bash
pip install objectpath requests
```

### Environment
- Python 3.x
- Elasticsearch and Kibana setup
- Valid email account for sending messages

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Configure Script Parameters**:
   - Update `recipients` with the email addresses of the recipients.
   - Update `sender_email` with the sender's email address.
   - Update `email_password` with the sender's email account password.
   - Update the `url` variable with your Kibana domain.
   - Update `header` with the correct `kbn-version` (your Kibana version).
   - Update the `files` list with the names of files to attach.
   - Provide Kibana `username` and `password` for authentication.
   - Update the `param1`, `param2`, and `filenames` variables with appropriate JSON query parameters and filenames.

3. **Set SMTP Details**:
   Update the `email_session` configuration to use your email service's SMTP server and port.

## Usage

1. Run the script using Python:
   ```bash
   python log_extractor.py
   ```

2. The script will:
   - Fetch log messages from Elasticsearch.
   - Save logs to specified text files.
   - Email the logs as attachments to the configured recipients.

## Example Output

### Log File Format
Extracted logs are saved in JSON format:
```json
[
  {
    "Total Count": [100]
  },
  {
    "Log 1": "Sample error message 1."
  },
  {
    "Log 2": "Sample error message 2."
  }
]
```

### Email Format
- **Subject**: Log report of [Date]
- **Body**:
  ```
  Dear people,

  Please find the Log report from Applications of [Date] attached with this mail.

  Thank you.

  Regards,
  Log Extractor Bot
  ```

## Security Considerations
- Avoid hardcoding sensitive information (e.g., passwords). Use environment variables or a configuration file instead.
- Ensure your Elasticsearch and Kibana setups are secure and accessible only to authorized users.

## Author
- **Name**: Arbin Khadka
- **Email**: arbin.khadka10@gmail.com

## License
This project is open source and available under the [MIT License](LICENSE).

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.
