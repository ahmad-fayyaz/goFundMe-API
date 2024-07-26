# GoFundMe Scraper API

This repository provides an API to fetch fundraisers from GoFundMe using Apify. The API is built using Django Ninja and allows users to search for fundraisers based on a query and limit the number of results.

## Features

- Fetch GoFundMe fundraisers based on a query.
- Limit the number of results returned.

## Prerequisites

- Python 3.7+
- Django
- Django Ninja
- Apify Client

## Setup

1. **Clone the repository**


2. **Create a virtual environment and activate it**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**


4. **Set up your environment variables**

   In api.py, add you Apify (free) API token. 

5. **Run the server**

    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the API docs at: http://127.0.0.1:8000/api/docs
and/or https://127.0.0.1:8000//api/funds?query=%3Cyour_query%3E&limit=%3Cyour_limit%3E


This was a quick sidequest for me. I needed such API for a project but could not find one. When I got to know how to build one, thought might make it public for anyone who wants it in the future.

Thank you for stopping by. 
