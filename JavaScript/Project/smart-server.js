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
        // Arahin ke halaman homepage
        response.writeHead(200, {"content-type" : "text/html"});
        response.end(
            `
            <h1>Selamat Datang di Serverku!</h1>
            <p>Ayo pilih menu yang tersedia!</p>
            <ul>
                <li>
                    <a href="/about">
                        /about
                    </a>
                    - Tentangku
                </li>

                <li>
                    <a href="/contact">
                        /contact
                    </a>
                    - Kontak
                </li>

                <li>
                    <a href="/api">
                        /api
                    </a>
                    - Data JSON
                </li>
            </ul>

            `
        );
    }

    else if (URL == '/about') {
        // Arahin ke halaman about
        response.writeHead(202, {"content-type" : "text/html"});
        response.end(
            `
            <h1>Halo, aku Naveria</h1>
            <p>Aku adalah seorang mahasiswa di Universitas Indonesia</p>
            <a href="/">Kembali ke halaman utama</a>
            `
        );
    }

    else if (URL == '/contact') {
        // Arahin ke halaman contact
        response.writeHead(202, {"content-type" : "text/html"});
        response.end(
            `
            <h1>Kontakku</h1>
            <p>email: belajar@backend.com</p>
            <a href="/">Kembali ke halaman utama</a>
            `
        );
    }

    else if (URL == '/api') {
        // API Endpoint : Kasih data JSON
        response.writeHead(202, {"content-type" : "application/json"});
        response.end(JSON.stringify({
            message: "Halo, ini aku dari API",
            data: {
                nama: "Delissesu",
                status: "Server belajar",
                versi: "1.0",
                hari: 2
            }}
        ));
    }

    else {
        // Handle 404 : URL ga ketemu
        response.writeHead(404, {"content-type": "text/html"});
        response.end(
            `
            <h1>404 : Halaman Tidak Ditemukan</h1>
            <p><strong>${URL}</strong> tidak ditemukan di server ini.</p>
            <a href="/">Kembali ke halaman utama</a>
            `
        );
    }
})

server.listen(3001, () => {
    console.log("Basic Smart Server Routing dan Response Running di Port 3001");  
    console.log("Coba akses web berikut: ");  
    console.log("- http://localhost:3001/");  
    console.log("- http://localhost:3001/about");  
    console.log("- http://localhost:3001/contact");  
    console.log("- http://localhost:3001/api");  
    console.log("- http://localhost:3001/random");  
})