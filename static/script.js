const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const button = document.getElementById("send-btn");

button.addEventListener("click", sendMessage);

input.addEventListener("keypress", function(event){
    if(event.key==="Enter"){
        sendMessage();
    }
});

async function sendMessage(){

    const message = input.value.trim();

    if(message==="") return;

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value="";

    chatBox.scrollTop = chatBox.scrollHeight;

    const response = await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="bot-message">
            ${data.reply}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

}