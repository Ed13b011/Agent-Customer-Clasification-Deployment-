# Agent-Customer-Clasification-Deployment

# Web App Applications: 
This Web App can be used to extract the information like Customer Sentiment, Improve Customer Satisfaction, Customer Feedback/Complaints, how Agents are handling Customer Queries, Improve Agent Performance
and other data driven actionable insights in Call Centers (Phone Support), Customer Service and other related companies where customers call in for help and call center representatives call out for sales, after sales, marketing, technical support services.
# Agent-Customer-IVR Conversation Examples:
1. Customer Uttetance: Don’t tell me what to do. Just tell me how you’re going to help me with my billing question?
2. Agent Utterance: It's a good day today at Bank of Wealth, my name is Heather, How can I help you?
3. IVR: We constantly endeavour to provide you with a world class customer service

# Steps for preparing Machine Learning Model:
1. Collect voice file of phone call conversation between agent and customer 
2. Split the voice file into small segements(chunks)
3. Run speech to text model (STT) on chunks to extract text
4. Prepare dataset by labelling the text. Labels are Agent, Customer, Interactive Voice Response(an automated telephony system)
5. Train Machine Learning Model on labelled dataset
6. Using this Model collect all Customer utterances for further analysis, Example: Customer Sentiment Analysis
7. Collect all Agent utterances for Agents Performance measurements and for any other analysis
