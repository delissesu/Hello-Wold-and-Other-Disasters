// Bisa pakai impor
// import http from 'node:http';

// Import module HTTP (built in di Node JS)
const http = require('http'); // Ga ada warning

// Buat servernya
const server = http.createServer((request, response) => {
    // Set header biar browser ngerti ini HTML
    response.writeHead(200, {'content-type':'text/html'});

    // Kasih response ke client
    response.end('<h1>Halo Naveria! Server pertamaku berhasil!</h1>');
});

// Run server di port 3000
server.listen(3000, () => {
    console.log('Server berjalan di Port 3000');
});