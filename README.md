# CDP_ChatBot

Chatbot is an **application of Artificial Intelligence, that interacts with the user, and answers the frequently asked questions**, frees the human resources to prioritize and focus on more critical tasks.

**In this project, the Chatbot answers "how-to" questions asked which are related to Customer Data Platforms.**

There are different types of Chatbots:

      1. FAQ Chatbot
      2. Recommendation Chatbot
      3. Customer Support Chatbot
      4. Context Aware Chatbot


Rough Idea, about the steps required for creation of a Chatbot:

      1. Requirement and Setup of a Development Environment.
      2. Problem Statement and Objective Definition.
      3. Pre-processing the collected or created Raw Data.
      4. Training a Machine Learning Model/Transformer. 
      5. Interface building.
      6. Testing

Here, for this project we are supposed to create a **context-aware chatbot**, where the chatbot is supposed to respond back the user queries, by extracting the relevant information from the documentations, handle cross-document queries and provide relevant feedback to irrelevant questions asked.

There are total of 4 Customer Data Platforms (CDP):
      
      1. Segment
      2. mParticle
      3. Lytics
      4. Zeotap

The job of Chatbot is to extract relevant information appropriately from each of the CDP's documentation, and guide the users to perform a task or achieve the desired output.

Core Capabilities of a Chatbot:

      1. Having a document knowledge-base to answer the questions.
      2. Answering the questions based on the given query/prompt.
      3. Cross-document comparison for fetching the data from multiple documents or comparing the data between documents.
      4. Handling errornous or irrelevant queries/prompts those which do not match with the given context.

Project Roadmap:

The plan is as follows:

  A. Data Preparation: 

      1. Extraction of relevant information from each of CDP's documentation.
            The data from the URL’s provided, can be extracted by making use of Web Scraping, which can be defined as the process of                         automatically extracting and storing huge amounts of data from the websites. 
            Libraries used: PyPDF2, requests, PDFPlumber, BeautifulSoup.

            The extracted data gets saved in .txt files. Once, we have the data prepared for us, we can go ahead with Indexing and Embedding.
       
  B. Indexing:

      1. Indexing facilitate fast and efficient retrieval of relevant information when users ask questions.
            Types:
               - TDIDF Indexing: Key-word based searches.
               - Embedding Indexing: Understand context and meaning.
  
           

  C. Querying: 
  
      1. Once, we have the cleansed documentation got indexed by TFIDF or Embedding we can proceed with Querying.
            It involves, providing prompts to the chatbot and looking if the chatbot answers them correctly.


  D. Front-end/UI Development:

      1. Flask is the lightweight frontend framework provided by Python Programming Language, that helps development of light weight web                  applications


Libraries to be used for this Project:

      1. pip install flask
      2. pip install requests beautifulsoup4
      3. pip install sentence-transformers
      4. pip install transformers
      5. from sklearn.metrics.pairwise import cosine_similarity
      6. from sklearn.feature_extraction.text import TfidfVectorizer
      

