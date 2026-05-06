# Grazioso Salvare Dashboard

## Project Overview

This project involved developing an interactive dashboard application for Grazioso Salvare to assist with managing and filtering animal shelter data used for search and rescue training. The dashboard integrates database functionality, data visualization, and user interaction tools to improve the efficiency of locating and analyzing rescue animals.

The application was designed to provide:
- searchable animal records
- rescue category filtering
- interactive charts and visualizations
- geographic mapping of selected animals
- database-driven dashboard interaction

## Technologies Used
- Python
- MongoDB
- Dash
- Plotly
- Jupyter Notebook
- CRUD Database Operations

## Features
- Interactive dashboard interface
- Search and rescue category filtering
- Dynamic animal record display
- Breed distribution pie charts
- Adjustable chart filtering options
- Geographic location mapping
- Reusable CRUD Python module for database interaction
- 
## Software Design & Maintainability

A major focus of this project was creating maintainable and reusable software components. A standalone CRUD Python module was developed to handle database operations and connect dashboard widgets to the MongoDB database.

This modular approach provided several advantages:
- simplified database interaction
- reusable code across dashboard components
- easier debugging and maintenance
- improved scalability for future features

The CRUD module was used throughout the dashboard to retrieve and manage animal records for tables, charts, and filtering systems. This design could also be extended in the future to support updating, deleting, or expanding rescue animal records.

## Problem Solving & Dashboard Design

One challenge during development involved designing data visualizations that remained readable when displaying large amounts of breed data. When all records were displayed at once, the charts became difficult to interpret due to the number of categories being visualized.

To improve usability, additional filtering options were implemented to allow users to display only the top 5, 10, 15, or all breeds within the dataset. This improved dashboard readability and overall user experience.

The project also introduced the use of Jupyter Notebook for dashboard development and testing, which differed from previous software projects and provided additional insight into interactive application development.

## What I Learned

Through this project I gained practical experience with:
- database-driven application development
- CRUD architecture
- dashboard and UI design
- data visualization
- client-focused software requirements
- modular software design
- usability improvements
- interactive filtering systems

This project reinforced the importance of designing software that is maintainable, adaptable, and user-focused while balancing technical functionality with usability.
