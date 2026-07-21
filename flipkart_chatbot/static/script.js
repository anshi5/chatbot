const input = document.getElementById("user-input");
const button = document.getElementById("send-btn");
const chatbox = document.getElementById("chat-box");

// send button
button.addEventListener("click", sendMessage);

// enter key
input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let message = input.value.trim();
    if (message === "") {
        return;
    }

    // user message
    chatbox.innerHTML += `
        <div class="user-message">
            <strong>You</strong>
            <p>${message}</p>
        </div>
    `;
    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    // flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
        // chatbot message
        .then(response => response.json())
        .then(data => {
            chatbox.innerHTML += `
                <div class="bot-message">
                    <strong>Bot</strong>
                    <p>${data.reply}</p>
                </div>
            `;
            chatbox.scrollTop = chatbox.scrollHeight;
        })
        // error handling
        .catch(error => {
            chatbox.innerHTML += `
                <div class="bot-message">
                    <strong>Bot</strong>
                    <p>Server error</p>
                </div>
            `;
            chatbox.scrollTop = chatbox.scrollHeight;
        });
}
