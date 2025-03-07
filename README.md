#  Hunter.io Tool For Open Web UI

This repository provides a tool to allow use of Hunter.io's Email Finder API directly within OpenWebUI to discover email addresses associated with domains and companies.

## Overview

This tool provides a seamless way to perform domain-to-email lookups using Hunter.io's Email Finder API without leaving your OpenWebUI environment. It enables you to find email addresses by domain name, company name, or individual's name with high confidence scores and verification status.

## Features

- Find email addresses using domain name and person's name
- Search by company name and person's name
- Look up emails using just a domain and full name
- Perform domain-wide email searches with customizable result limits
- View confidence scores and verification status for each result
- See additional information like position and company when available
- Check source count for discovered email addresses

## Requirements

- OpenWebUI version 0.4.0 or higher
- Hunter.io API key (get one at https://hunter.io/users/sign_up)
- Python `requests` library

## Installation

1. Add this tool to your OpenWebUI installation
2. Configure your Hunter.io API key in the tool settings (passed as a valve)

## Usage

The tool provides several functions for different email lookup scenarios:

### Find Email by Domain and Name

```
find_email_by_domain_and_name(domain, first_name, last_name)
```

### Find Email by Company and Name

```
find_email_by_company_and_name(company, first_name, last_name)
```

### Find Email by Full Name

```
find_email_by_full_name(domain, full_name)
```

### Domain Search

```
domain_search(domain, limit=10)
```

## Customization

The tool can be modified to optimize:
- Retrieval format: Adjust the API parameters in the request functions
- Presentation format: Modify the formatting of results in each function's return statement

## Version

Current version: 1.0.0

## License

MIT License

## Author

Daniel Rosehill  
GitHub: [https://github.com/danielrosehill](https://github.com/danielrosehill)

## Repository

GitHub: [https://github.com/danielrosehill/Openwebui-Hunter-Tool](https://github.com/danielrosehill/Openwebui-Hunter-Tool)
