// توابع برای باز و بسته کردن پنل چت
function toggleChat() {
    var chatContainer = document.getElementById("chat-container");

    // بررسی اینکه آیا پنل چت باز است یا بسته
    if (chatContainer.style.display === "none" || chatContainer.style.display === "") {
        chatContainer.style.display = "flex";  // پنل چت باز می‌شود
    } else {
        chatContainer.style.display = "none";  // پنل چت بسته می‌شود
    }
}

// بستن پنل چت اگر کاربر در هر نقطه از صفحه کلیک کند
document.addEventListener("click", function (event) {
    var chatContainer = document.getElementById("chat-container");
    var chatButton = document.querySelector(".chat-button");

    // اگر کلیک خارج از پنل چت یا دکمه چت باشد، پنل بسته شود
    if (!chatContainer.contains(event.target) && !chatButton.contains(event.target)) {
        chatContainer.style.display = "none";
    }
});

// ارسال پیام
function sendMessage() {
    var message = document.getElementById("chat-input").value;
    if (message.trim()) {
        var chatBox = document.getElementById("chat-box");
        var newMessage = document.createElement("div");
        newMessage.textContent = "شما: " + message;
        chatBox.appendChild(newMessage);
        document.getElementById("chat-input").value = ""; // پاک کردن متن وارد شده
        chatBox.scrollTop = chatBox.scrollHeight; // اسکرول به پایین پنل چت
    }
}

// ارسال پیام با فشار دادن کلید Enter
document.getElementById("chat-input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // جلوگیری از رفتن به خط جدید
        sendMessage(); // ارسال پیام
    }
});
