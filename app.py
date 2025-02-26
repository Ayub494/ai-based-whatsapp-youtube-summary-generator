from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from summarizeVideo import summarize_youtube_video
 
app = Flask(__name__)
 
@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    # Get the incoming message text and sender's WhatsApp number
    incoming_message = request.form.get('Body')
    sender_number = request.form.get('From')
 
    print(f"Received message from {sender_number}: {incoming_message}")
 
    # Create a response object
    response = MessagingResponse()
 
    # Logic to handle different messages
    if incoming_message:
        response.message("Hello Ayyub! I am generating your summary please wait...")
        try:
            # Pass the URL to the summarize function
            summary = summarize_youtube_video(incoming_message)
            # Send the summary as the response
            response.message(f"Here is the summary:\n\n{summary}")
        except Exception as e:
            # Handle errors (e.g., invalid URL, issues with the summarization)
            response.message(f"Sorry, I couldn't summarize the video. Error: {str(e)}")
    else:
        response.message("Sorry, I didn't understand that. I couldn't summarize the video ")
 
 
    return str(response)
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)