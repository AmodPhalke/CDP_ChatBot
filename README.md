# CDP_ChatBot

Chatbot is an **application of Artificial Intelligence, that interacts with the user, and answers the frequently asked questions**, frees the human resources to prioritize and focus on more critical tasks.

**In this project, the Chatbot answers "how-to" questions asked which are related to Customer Data Platforms.**

There are different types of Chatbots:

      1. FAQ Chatbot
      2. Recommendation Chatbot
      3. Customer Support Chatbot
      4. Context Aware Chatbot

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

  A. Processing - Parse the documents, and make use of NLP for extraction of relevant information. 

      1. Extraction of relevant information from each of CDP's documentation.
            Extraction of data could be possible by making use of libraries like:
            a. HTML/Webpage based Data: BeautifulSoup.
            b. PDF Data: PyPDF2, pdfplumber.
            
      2. Summarization of retreived data (Extractive Summarization) can be performed by making use of Transformers. 
            Here, transformers are the class of deep learning models, mostly used for NLP that make use of Attention Mechanism.  

  B. Indexing - Also, convert textual data into numerical data by making use of Semantic Embeddings that facilitates easy querying.
  
      1. Conversion of extracted data into embeddings for easy and efficient querying.
            Embeddings can be defined as the numerical representations of textual data in a high-dimensional space. 
            These embeddings helps the computers in understanding meaning, context and relationships of words and sentences.
            Libraries for performing Semantic Embeddings:
            a. sentence-transformers
            b. OpenAI GPT Embeddings

  C. Understanding - Making use of NLP models to understand the input prompts/queries. This helps in classification of queries - Irrelevant or Relevant. 
  
      1. Understanding the input query using Intents and Pre-trained models.
            Pre-trained Models like GPT2, GPT3 etc. can be used to classify the queries as Relevant and Irrelevant.
            
      2. Retreival of relevant content.
            The goal is to make use of cosine similarity, to match the input queries with document embeddings. 
            Here, cosine similarity refers to a metric, that focuses on Direction and not on the Magnitude, making it ideal for text-based applications.
            
      3. Handling Irrelevant requests and Cross-Document queries.


Libraries to be used for this Project:

      1. pip install flask
      2. pip install requests beautifulsoup4
      3. pip install sentence-transformers
      4. pip install transformers
      5. pip install transformers torch scikit-learn

