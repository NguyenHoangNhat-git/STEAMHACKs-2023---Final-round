const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;

const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat-room/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    if (data.message){
        const chatBox = document.getElementById("chatBox");
        const current_user_id = JSON.parse(document.getElementById('current-user-id').textContent);
        

        const newMessageDiv = document.createElement("div");
        const newMessage = document.createElement("div");
        if (current_user_id == data.sender_id){
            newMessageDiv.classList.add("message", "align-user-message");
            newMessage.classList.add("user-message");
        }
        else {
            newMessageDiv.classList.add("message");
            newMessage.classList.add("other-message");
        }
        newMessage.innerHTML = data.message;
        newMessageDiv.appendChild(newMessage);
        chatBox.appendChild(newMessageDiv);
        
        chatBox.scrollTop = chatBox.scrollHeight;
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};