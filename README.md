# ai-based-whatsapp-youtube-summary-generator
🚀 Introducing the AI-Based WhatsApp YouTube Summary Generator! 🎥🤖 Tired of watching long YouTube videos just to get the key insights? I built an AI-powered solution that summarizes YouTube videos instantly via WhatsApp! 📩

Setup

Create a virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Set environment variables: Create a .env file in the project root directory and add your Twilio and api keys:

Note: For api key used together.ai and used model 
meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
TOGETHER_AI_API_KEY=api_key

	

Run the Flask server:
flask run

Set up the Twilio webhook:
Set up an twilio account 
Set your ngrok URL as the webhook for incoming messages from Twilio.
Ngrok provides a public URL to your local server, allowing Twilio to send webhook requests to your backend running on your local machine.
Example: https://your_ngrok_url/whatsapp

Test with WhatsApp:
Send a YouTube video URL to your Twilio WhatsApp number.
The bot will respond with a summary of the video.

