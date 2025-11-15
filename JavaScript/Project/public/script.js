function showMessage() {
    const messages = [
        "Halo! Server file bekerja dengan baik!",
        "JavaScript client-side berfungsi!",
        "Keren! Semua file ter-load dengan proper!",
        "Node.js + Static Files = Powerful!"
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    document.getElementById('message').textContent = randomMessage;
}