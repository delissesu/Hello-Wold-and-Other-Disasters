// Import module HTTP (built in di Node JS)
const http = require('http');

// Buat servernya
const server = http.createServer((request, response) => {

    // Get URL yang diminta
    const URL = request.url;
    const METHOD = request.method;

    // Logging
    console.log(`Request => ${METHOD} : ${URL}`);

    // Routing : Kasih respons berdasarkan URL
    if (URL === '/' && METHOD === 'GET') {

        // API Endpoint : Kasih data JSON
        response.writeHead(200, {"content-type" : "application/json"});

        response.end(JSON.stringify(
            {
                message: "Halo, ini aku dari API",
                data: {
                    nama: "Delissesu",
                    status: "Server belajar",
                    versi: "1.0",
                    hari: 2
                }
            }
        ));
    }

    else {
        // Handle 404 : URL ga ketemu
        response.writeHead(404, {"content-type": "text/html"});
        response.end(
            `
            <h1>404 : Halaman Tidak Ditemukan</h1>
            <p><strong>${URL}</strong>tidak ditemukan di server ini.</p>
            <a href="/">Kembali ke halaman utama</a>
            `
        );
    }
})