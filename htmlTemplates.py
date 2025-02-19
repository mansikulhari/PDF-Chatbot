css = '''
<style>
.chat-message {
    padding: 1rem;
    margin-bottom: 1rem;
    display: flex;
    border: 2px solid #ccc;
    border-radius: 0.5rem;
}

.chat-message.user {
    background-color: #f0f0f0;
    border-color: #ccc;
}

.chat-message.bot {
    background-color: #007bff;
    color: #fff;
    border-color: #007bff;
}

.chat-message .avatar {
    width: 20%;
    padding: 1rem;
}

.chat-message .avatar img {
    max-width: 50px;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 1rem;
    color: #333;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Chatbot_img.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
