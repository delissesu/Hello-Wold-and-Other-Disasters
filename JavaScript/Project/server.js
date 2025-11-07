// Bisa pakai impor
// import http from 'node:http';

// Non Blocking
console.log("Delion : Start Journey!")

// Import module HTTP (built in di Node JS)
const http = require('http'); // Ga ada warning

// Buat servernya
const server = http.createServer((_request, response) => {
    // Set header biar browser ngerti ini HTML
    response.writeHead(200, {'content-type':'text/html'});

    response.write('Coba tes, ini nongol apa ga?')

    // Kasih response ke client
    response.end('<h1>Halo Naveria! Server pertamaku berhasil!</h1>');
});

// Run server di port 3000
server.listen(3000, () => {
    console.log('Server berjalan di Port 3000');
});

// Non Blocking
console.log("Delion : End!")

// Kondisi kalau port udah dipake (handling)
server.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
        console.log("Port 3000 sudah dipakai!")
    }
})