from browser_use import Agent , ChatGoogle
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    api_key = os.getenv('GOOGLE_API_KEY')
    llm = ChatGoogle('gemini-2.5-flash' , api_key=api_key)
    task = "Search Google for 'which are the top Deep Learning Certifictaion Courses?' and give me only top 3 of them"
    agent = Agent( llm=llm , task=task)
    history = await agent.run()
    print(history.urls())

if __name__ == "__main__":
    asyncio.run(main())


################################------------------------------------LOG RECORDS----------------------------------########################################

# PS C:\Users\Admin\Desktop\GeekForGeeks\Projects\Day-20> python day20_browser_agent.py 
# INFO     [service] Using anonymized telemetry, see https://docs.browser-use.com/development/telemetry.
# INFO     [Agent] 🚀 Task: Search Google for 'which are the top Deep Learning Certifictaion Courses?' and give me only top 3 of them
# INFO     [service] ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# INFO     [service] 🔐 To view this run in Browser Use Cloud, authenticate with:
# INFO     [service]     👉  browser-use auth
# INFO     [service]     or: python -m browser_use.cli auth
# INFO     [service] ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

# INFO     [Agent] 🧠 Starting a browser-use version 0.7.10 with model=gemini-2.5-flash
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 1:
# INFO     [Agent]   👍 Eval: Agent initialized. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Search Google for 'which are the top Deep Learning Certifictaion Courses?'
# INFO     [Agent]   🦾 [ACTION 1/1] search: query: which are the top Deep Learning Certifictaion Courses?, search_engine: google
# ERROR    [cdp_use.client] CDP Error for request 31: {'code': -32000, 'message': 'Not attached to an active page'}
# INFO     [tools] 🔍  Searched Google for 'which are the top Deep Learning Certifictaion Courses?'
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 2:
# INFO     [Agent]   👍 Eval: Successfully searched Google for 'which are the top Deep Learning Certifictaion Courses?'. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Identify the most relevant link from the search results that lists deep learning certification courses and click on it to gather the information.
# INFO     [Agent]   🦾 [ACTION 1/1] click_element_by_index: index: 37, while_holding_ctrl: False
# INFO     [tools] 🖱️ Clicked element
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 3:
# INFO     [Agent]   👍 Eval: Successfully navigated to the Coursera page for Deep Learning courses. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Scroll down the page to view more courses and then extract the top 3 deep learning certification courses using `extract_structured_data`.
# INFO     [Agent]   🦾 [ACTION 1/1] scroll: down: True, num_pages: 2.0, frame_element_index: None
# INFO     [tools] 🔍 Scrolled down the page by 2.0 pages (requested: 2.0, 788px per page)
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 4:
# INFO     [Agent]   ⚠️ Eval: Failed to navigate to the Coursera page. I am still on the Google search results page. Verdict: Failure
# INFO     [Agent]   🎯 Next goal: Identify a relevant link from the current Google search results that lists deep learning certification courses and click on it to gather the information.
# INFO     [Agent]   🦾 [ACTION 1/1] click_element_by_index: index: 19, while_holding_ctrl: False
# INFO     [tools] 🖱️ Clicked element
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 5:
# INFO     [Agent]   👍 Eval: The previous evaluation was incorrect. I successfully navigated to the Coursera page. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Scroll down the page to view more courses and then extract the top 3 deep learning certification courses using `extract_structured_data`.
# INFO     [Agent]   🦾 [ACTION 1/1] scroll: down: True, num_pages: 2.0, frame_element_index: None
# INFO     [tools] 🔍 Scrolled down the page by 2.0 pages (requested: 2.0, 788px per page)
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 6:
# INFO     [Agent]   👍 Eval: Successfully scrolled down the page to view more courses. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Click on the 'Professional Certificates' filter to narrow down the search results to only certification courses, then extract the top 3 courses.
# INFO     [Agent]   🦾 [ACTION 1/1] click_element_by_index: index: 470, while_holding_ctrl: False
# WARNING  [BrowserSession] No visible quad found, using first quad
# INFO     [tools] 🖱️ Clicked element
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 7:
# INFO     [Agent]   👍 Eval: Successfully clicked on the 'Professional Certificates' filter. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Extract the top 3 deep learning certification courses from the filtered results using `extract_structured_data`.
# INFO     [Agent]   🦾 [ACTION 1/1] extract_structured_data: query: Extract the top 3 deep learning certification courses including their titles, providers, ratings, and
# INFO     [tools] 📄 <url>
# https://www.coursera.org/courses?query=deep%20learning
# </url>
# <query>
# Extract the top 3 deep learning certification courses including their titles, providers, ratings, and number of reviews.
# </query>
# <result>
# 1. **Deep Learning**
#    * Provider: DeepLearning.AI
#    * Rating: 4.8 out of 5 stars
#    * Number of reviews: 147K
# 2. **Neural Networks and Deep Learning**
#    * Provider: DeepLearning.AI
#    * Rating: 4.9 out of 5 stars
#    * Number of reviews: 123K
# 3. **Convolutional Neural Networks**
#    * Provider: DeepLearning.AI
#    * Rating: 4.9 out of 5 stars
#    * Number of reviews: 43K
# </result>
# INFO     [Agent] 

# INFO     [Agent] 📍 Step 8:
# INFO     [Agent]   👍 Eval: Successfully extracted the top 3 deep learning certification courses. Verdict: Success
# INFO     [Agent]   🎯 Next goal: Provide the extracted information to the user and mark the task as complete.
# INFO     [Agent]   🦾 [ACTION 1/1] done: text: Here are the top 3 Deep Learning Certification Courses I found on Coursera:\n\n1. **Deep Learning**\n   * Provider: DeepL
# INFO     [Agent] 
# 📄  Final Result:
# Here are the top 3 Deep Learning Certification Courses I found on Coursera:

# 1. **Deep Learning**
#    * Provider: DeepLearning.AI
#    * Rating: 4.8 out of 5 stars
#    * Number of reviews: 147K
# 2. **Neural Networks and Deep Learning**
#    * Provider: DeepLearning.AI
#    * Rating: 4.9 out of 5 stars
#    * Number of reviews: 123K
# 3. **Convolutional Neural Networks**
#    * Provider: DeepLearning.AI
#    * Rating: 4.9 out of 5 stars
#    * Number of reviews: 43K


################################------------------------------------OUTPUT----------------------------------########################################


# INFO     [Agent] ✅ Task completed successfully
# WARNING  [cdp_use.client] WebSocket connection closed: no close frame received or sent
# ['about:blank', 'https://www.google.com/search?q=which+are+the+top+Deep+Learning+Certifictaion+Courses%3F&udm=14', 'https://www.coursera.org/courses?query=deep%20learning', 'https://www.google.com/search?q=which+are+the+top+Deep+Learning+Certifictaion+Courses%3F&udm=14&sei=vnrdaMaQMLDn1e8P7K__oAY', 'https://www.coursera.org/courses?query=deep%20learning', 'https://www.coursera.org/courses?query=deep%20learning', 'https://www.coursera.org/courses?query=deep%20learning', 'https://www.coursera.org/courses?query=deep%20learning']
# Unclosed client session
# client_session: <aiohttp.client.ClientSession object at 0x0000024FAC085D10>
# Unclosed connector
# connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x0000024FAC49B650>, 1320189.079642)])']
# connector: <aiohttp.connector.TCPConnector object at 0x0000024FABFD3750>
# PS C:\Users\Admin\Desktop\GeekForGeeks\Projects\Day-20>







