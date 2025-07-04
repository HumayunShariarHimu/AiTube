from flask import Flask, render_template, request
from ai.script_gen import generate_script
from ai.tts_gen import generate_voice
from ai.video_gen import make_video
from ai.meta_gen import generate_metadata
from ai.youtube_upload import youtube_authenticate, upload_video

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]
    
    script = generate_script(topic)
    generate_voice(script)
    make_video()
    
    title, description, tags = generate_metadata(topic)
    
    youtube = youtube_authenticate()
    upload_video(youtube, "final_video.mp4", title, description, tags)

    return f"✅ ভিডিও সফলভাবে ইউটিউবে আপলোড হয়েছে!"

if __name__ == "__main__":
    app.run(debug=True)
