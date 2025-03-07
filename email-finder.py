"""
title: Hunter Email Finder
author: Daniel Rosehill
author_url: https://github.com/danielrosehill
git_url: https://github.com/danielrosehill/Enrichso-Openwebui
description: Find email addresses using Hunter.io's Email Finder API
required_open_webui_version: 0.4.0
requirements: requests
version: 1.0.0
license: MIT
"""

import os
import requests
import json
from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field

class Tools:
    class Valves(BaseModel):
        api_key: str = Field(
            default="", 
            description="Your Hunter.io API key. Get one at https://hunter.io/users/sign_up"
        )
    
    def __init__(self):
        """Initialize the Tool."""
        self.valves = self.Valves()
        self.api_base_url = "https://api.hunter.io/v2"
    
    def find_email_by_domain_and_name(self, domain: str, first_name: str, last_name: str) -> str:
        """
        Find an email address using a domain and a person's name.
        
        :param domain: The domain name to search (e.g., 'example.com')
        :param first_name: The first name of the person
        :param last_name: The last name of the person
        :return: A formatted string with the email information
        """
        if not self.valves.api_key:
            return "Error: API key is required. Please set your Hunter.io API key in the tool settings."
        
        endpoint = f"{self.api_base_url}/email-finder"
        params = {
            "domain": domain,
            "first_name": first_name,
            "last_name": last_name,
            "api_key": self.valves.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data and 'email' in data['data']:
                email_data = data['data']
                result = f"Email found: {email_data['email']}\n"
                result += f"Confidence score: {email_data['score']}%\n"
                
                if 'verification' in email_data and 'status' in email_data['verification']:
                    result += f"Verification status: {email_data['verification']['status']}\n"
                
                if 'position' in email_data and email_data['position']:
                    result += f"Position: {email_data['position']}\n"
                
                if 'company' in email_data and email_data['company']:
                    result += f"Company: {email_data['company']}\n"
                
                if 'sources' in email_data and email_data['sources']:
                    result += f"Found in {len(email_data['sources'])} sources\n"
                
                return result
            else:
                return f"No email found for {first_name} {last_name} at {domain}."
        except requests.RequestException as e:
            return f"Error fetching email: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def find_email_by_company_and_name(self, company: str, first_name: str, last_name: str) -> str:
        """
        Find an email address using a company name and a person's name.
        
        :param company: The company name to search
        :param first_name: The first name of the person
        :param last_name: The last name of the person
        :return: A formatted string with the email information
        """
        if not self.valves.api_key:
            return "Error: API key is required. Please set your Hunter.io API key in the tool settings."
        
        endpoint = f"{self.api_base_url}/email-finder"
        params = {
            "company": company,
            "first_name": first_name,
            "last_name": last_name,
            "api_key": self.valves.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data and 'email' in data['data']:
                email_data = data['data']
                result = f"Email found: {email_data['email']}\n"
                result += f"Confidence score: {email_data['score']}%\n"
                
                if 'verification' in email_data and 'status' in email_data['verification']:
                    result += f"Verification status: {email_data['verification']['status']}\n"
                
                if 'position' in email_data and email_data['position']:
                    result += f"Position: {email_data['position']}\n"
                
                if 'company' in email_data and email_data['company']:
                    result += f"Company: {email_data['company']}\n"
                
                if 'sources' in email_data and email_data['sources']:
                    result += f"Found in {len(email_data['sources'])} sources\n"
                
                return result
            else:
                return f"No email found for {first_name} {last_name} at {company}."
        except requests.RequestException as e:
            return f"Error fetching email: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def find_email_by_full_name(self, domain: str, full_name: str) -> str:
        """
        Find an email address using a domain and a person's full name.
        
        :param domain: The domain name to search (e.g., 'example.com')
        :param full_name: The full name of the person
        :return: A formatted string with the email information
        """
        if not self.valves.api_key:
            return "Error: API key is required. Please set your Hunter.io API key in the tool settings."
        
        endpoint = f"{self.api_base_url}/email-finder"
        params = {
            "domain": domain,
            "full_name": full_name,
            "api_key": self.valves.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data and 'email' in data['data']:
                email_data = data['data']
                result = f"Email found: {email_data['email']}\n"
                result += f"Confidence score: {email_data['score']}%\n"
                
                if 'verification' in email_data and 'status' in email_data['verification']:
                    result += f"Verification status: {email_data['verification']['status']}\n"
                
                if 'position' in email_data and email_data['position']:
                    result += f"Position: {email_data['position']}\n"
                
                if 'company' in email_data and email_data['company']:
                    result += f"Company: {email_data['company']}\n"
                
                if 'sources' in email_data and email_data['sources']:
                    result += f"Found in {len(email_data['sources'])} sources\n"
                
                return result
            else:
                return f"No email found for {full_name} at {domain}."
        except requests.RequestException as e:
            return f"Error fetching email: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def domain_search(self, domain: str, limit: int = 10) -> str:
        """
        Find all email addresses for a domain.
        
        :param domain: The domain name to search (e.g., 'example.com')
        :param limit: Maximum number of results to return (default: 10)
        :return: A formatted string with the domain email information
        """
        if not self.valves.api_key:
            return "Error: API key is required. Please set your Hunter.io API key in the tool settings."
        
        endpoint = f"{self.api_base_url}/domain-search"
        params = {
            "domain": domain,
            "limit": limit,
            "api_key": self.valves.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data and 'emails' in data['data']:
                emails = data['data']['emails']
                if not emails:
                    return f"No email addresses found for domain {domain}."
                
                result = f"Hunter Email Finder\n"
                result += f"I found {len(emails)} email addresses for {domain}:\n\n"
                
                # Create a table header
                result += "| Name | Title | Email |\n"
                result += "|------|-------|-------|\n"
                
                # Add each email as a row in the table
                for email in emails:
                    name = ""
                    if 'first_name' in email and 'last_name' in email:
                        name = f"{email.get('first_name', '')} {email.get('last_name', '')}"
                    else:
                        name = "Unknown"
                    
                    position = email.get('position', 'Unknown')
                    email_address = email.get('value', 'N/A')
                    
                    result += f"| {name} | {position} | {email_address} |\n"
                
                # Add organization if available
                if 'domain' in data['data'] and 'organization' in data['data']['domain']:
                    result += f"\nOrganization: {data['data']['domain']['organization']}"
                
                return result
            else:
                return f"No email addresses found for domain {domain}."
        except requests.RequestException as e:
            return f"Error fetching domain emails: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
