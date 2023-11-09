# Whatcom County Hearing Examiner Enhanced Search

Access it live <a href='http://whatcomhesearch.us-west-2.elasticbeanstalk.com/'>here</a>.

## About

<em>This is a filtered search platform for publically available Whatcom County Hearing Examiner decisions. It was created in response to the needs of the Land Use team at a local law firm. Although the published decisionss are availble on the Whatcom County website, the archive search functionality is limited. This resulted in a time consuming process requiring attorneys and paralegals to manually search through the archive to find relevant decisions. This platform addresses that issue by providing a fast and simple way to search through decisions by keyword, date, and the name of the Hearing Examiner who issued the decision.</em>

<img width="1398" alt="Screenshot 2023-09-29 at 6 09 53 PM" src="https://github.com/AaronAWB/Whatcom_HE_Search/assets/108595340/e8a9c3f5-438a-4fec-a024-675190e3b9a8">

## What is the Whatcom County Hearing Examiner?

The Hearing Examiner is a quasi-judicial officer appointed by the Whatcom County Council to hear and decide land use appeals, development proposals, and other matters. Common land use matters heard by the Hearing Examiner include:
* Zoning
* Shoreline Management
* Variances
* Premliminary plats
* Appeals from county determinations regarding whether a project requires an environmental impact statement
* Appeals of county administrative determinations involving the various land use regulatory codes and policies of the county, including the Shoreline Management Program

This Hearing Examiner applies laws and ordinances passed by the County Council. The Hearing Examiner's decisions are public records and are valuable to attorneys and other professionals involved in land use matters as well as the general public.

## Technologies and Tools

### Client

The web client is a simple platform for displaying data extracted from the Whatcom County website and stored in a PostgreSQL database for fast retrieval.

* Written with HTML, CSS, and TypeScript, using the React framework.
* Setup was done using Vite as an alternative to Create React App, allowing aliases for cleaner imports and faster build times.
* Styling relies primarily on React Bootstrap.
* Pages are routed using React Router.
* HTTP calls to the server's REST API are made using the Axios library.

### Server

* Written in Python using the Flask framework.
* REST API is built using Flask-RESTX.
* Database queries - including search filters - are handled using the SQLAlchemy ORM.
* The app is served using Gunicorn and hosted on AWS Elastic Beanstalk.
* Data is stored in a PostgreSQL database hosted on elephantsql.com.

### Data Extraction

This website relies on data extracted from the Whatcom County website and the Hearing Examiner decisions themselves, which are available on the County's website in PDF format. The data extraction process is handled by a separate Python script, which is run periodically to update the database with new decisions. The script uses the following libraries:

* BeautifulSoup for parsing links to the decisions from the County's website.
* PyPDF2 for extracting text from the decisions saved in searchable PDF format.
* Ocrmypdf for converting non-searchable PDFs to searchable PDFs using Google's Tesseract OCR engine.

## Technical Challenges

Collecting accurate and complete data on each decision was essential to this project. The following are some of the challenges I encountered and how I addressed them.

### Locating the Decisions

Links to the decisions in PDF format are available on the County's website but are displayed in a lengthly table. Some table entries identify the Hearing Date and Decision Date while others do not. Fortunately, the table entries follow a consistent HTML format that can be parsed using BeautifulSoup. This allows the Python script to programmaticaly assemble and access links to every decision.

Similarly, the Python script uses BeautifulSoup to parse the table for Hearing Dates and Decision dates for the cases where that information was identified on the website. 

### Extracting Text from the Decisions

Other relevant information for each decision is contained in the text of the decision itself. This includes the name of the Hearing Examiner who issued the decision and the full text of the decision (necessary for keyword searches).

I used the PyPDF2 library to extract the text from the PDFs located at each link. However, because different processes were used by County staff to scan and upload the decisions, many of the PDFs were not searchable. This meant that the text was not stored in the PDF itself but was instead rendered as an image, making extraction impossible using PyPDF2. 

To address this issue, I used the Ocrmypdf library to convert the non-searchable PDFs to searchable PDFs using Google's Tesseract OCR engine. This allowed me to extract the text of every decision. The downside to this approach is that due to formatting issues, the text extracted by Tesseract contains occassional errors, especially if the original document was scanned at a low resolution. However, the errors are relatively minor and do not have a significant impact on keyword seach functionality.

### Locating the Hearing Examiner's Name

The name of the Hearing Examiner who issued the decision is included in the decision but is not listed on the website. To locate the name, my Python script finds the decision's signature block using a regular expression match. This approach, although sucessfully in many cases, is not perfect. The regular expression needed to account for the fact that the signature block is not always formatted the same way. 

For example, some followed the format of "DATED this 1st day of January, 2021," while others were formatted as "DATED this 1st day of January, 2021. by Hearing Examiner John Doe." The regular expression I used to locate the signature block was able to account for these differences but missed certain less common variations or was unable to read the signature block if the decision was scanned at a low resolution. To address this issue, I manually reviewed the decisions that were not matched and updated the database with the correct name.

## Future Improvements

In addition to making it faster and easier to locate relevate Whatcom County Hearing Examiner decisions, the goal for this platform is to provide additional ways for legal professionals and the publice to interact with the data using AI. This may involve the use of tools such as the ChatGPT API to generate summaries of decisions, answer targeted queries, or search decisions using natural language prompts.

## Author

Aaron Brinckerhoff | Full Stack Software Developer | <a href='https://www.linkedin.com/in/aaron-brinckerhoff-6b9a5340/'>LinkedIn</a> | <a href='https://www.aaronbrinckerhoff.dev/'>Portfolio</a>
