'''
Server.py
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Analyze text
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    #Check if text to analyze 
    if not text_to_analyze:
        return 'No text provided', 400
    
    formated_response = emotion_detector(text_to_analyze)


    if not formated_response['dominant_emotion']:
        return 'Invalid or nonexistent text'

    return (
        f"For the given statement, the system response is 'anger' : {formated_response['anger']}, "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    '''
    Index rendering
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)