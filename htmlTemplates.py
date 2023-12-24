css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/R.e81d0639d1c650744a0040117bfd3aa1?rik=XFXebydpnkqb9A&riu=http%3a%2f%2fwww.sunriserobot.net%2fimages%2fassets%2frobot_circle.png&ehk=Il7Vw8TH3DOjYO2Rdj1My9NszWjFVEOLA5AWq4worgo%3d&risl=&pid=ImgRaw&r=0">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://c2.staticflickr.com/6/5284/5351765904_0fea8b6296_b.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
