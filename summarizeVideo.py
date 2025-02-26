from langchain_together import ChatTogether
from langchain_community.document_loaders import YoutubeLoader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from IPython.display import Markdown, display
from dotenv import load_dotenv
import os
 
load_dotenv()
 
api_key = os.getenv('API_KEY')
 
def summarize_youtube_video(video_url):
    """
    Summarizes a YouTube video transcript using LangChain and displays
    the summary as Markdown.
    """
    # Initialize the LLM
    llm = ChatTogether(
        api_key=api_key,
        temperature=0.0,
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
    )
 
    # Load the video transcript
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
    data = loader.load()
 
    # Define the prompt template
    product_description_template = PromptTemplate(
        input_variables=["video_transcript"],
        template="""
        Read through the entire transcript carefully.
        Provide a concise summary of the video's main topic and purpose.
        Extract and list the five most interesting or important points from the transcript.
        For each point: State the key idea in a clear and concise manner.
 
        - Ensure your summary and key points capture the essence of the video without including unnecessary details.
        - Use clear, engaging language that is accessible to a general audience.
        - If the transcript includes any statistical data, expert opinions, or unique insights,
          prioritize including these in your summary or key points.
 
        Video transcript: {video_transcript}    
        """
    )
 
    pipeline = product_description_template | llm
 
    # Generate the summary
    response = pipeline.invoke({"video_transcript": data[0].page_content})
    summary_text = response.content
 
    display(Markdown(summary_text))
    
    return summary_text