const socket = new WebSocket("ws://localhost:8000/ws");

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const form = document.getElementById("message-form");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

function addMessage(text, type) {
    const item = document.createElement("li");
    const time = new Date().toLocaleTimeString();
    item.className = type;
    item.textContent = `[${time}] ${text}`;
    messagesEl.appendChild(item);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function setStatus(text, online) {
    statusEl.textContent = text;
    statusEl.className = online ? "status online" : "status offline";
    sendButton.disabled = !online;
}

socket.onopen = () => {
    setStatus("Connecté", true);
    addMessage("Connexion établie", "info");
};

socket.onmessage = (event) => {
    addMessage(`Serveur : ${event.data}`, "received");
};

socket.onclose = () => {
    setStatus("Déconnecté", false);
    addMessage("Connexion perdue", "info");
};

socket.onerror = () => {
    addMessage("Erreur de connexion", "info");
};

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value;
    if (text.trim() === "" || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    addMessage(`Moi : ${text}`, "sent");
    input.value = "";
    input.focus();
});
