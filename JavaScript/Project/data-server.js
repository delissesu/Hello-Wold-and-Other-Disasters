// Hari 3: "Data Handler" - Processing Request Data & POST Handling

const http = require('http');
const querystring = require('querystring');
const { URLSearchParams } = require('url');

const server = http.createServer((request, response) => {
    const { url, method } = request;

    console.log(`${method} : ${url}`);

    // Handle GET request : search/query parameter
    if (method === 'GET' && url.includes('/search')) {

        // Ekstrak query parameter dari URL
        const queryString = url.split('?')[1];

        // Logging
        console.log(queryString);
        console.log(queryString[0]);
        console.log(queryString[1]);
        
        // const searchParameter = [[queryString, 'value'], [keyword, category]];
        // new URLSearchParams(searchParameter);

        if (queryString && queryString.trim() !== '') {
            const searchParameter = new URLSearchParams(queryString);
            const keyword = searchParameter.get('q') || 'tidak ada keyword';
            const category = searchParameter.get('category') || 'all';

            response.writeHead(200, { "content-type" : "text/html" });
            response.end(
                `
                <h1>Hasil Pencarian</h1>
                <p>Keyword: <strong>${keyword}</strong></p>
                <p>Category: <strong>${category}</strong></p>
                <br>
                <a href="/">Kembali ke menu utama</a>
                `
            );
        } 
        else {
            response.writeHead(400, {"content-type" : "text/html"});
            response.end(
                `
                <h1>
                    400 : Bad Request
                </h1>

                <p>
                    Query parameter tidak ditemukan.
                </p>
                `
            )
        }

    }

    // Handle POST request : form submission
    else if (method === 'POST' && url === '/login') {
        let body = '';
        /*
        - Request adalah event emitter (bisa emit events)
        - Jadi, perlu sesuatu yang listen ke eventnya
        */

        // Accept data yang dikirim client (chunk by chunk)
        // Listen channel data : kirim data
        request.on('data', chunk => {
            // Logging
            console.log(`Cek chunk: ${chunk} dan Cek body ${body}`);
            body += chunk.toString();
        })

        // Semua data sudah diterima : data sudah selesai dikirim
        request.on('end', () => { // Listen channel end
            // Logging
            console.log(`Cek body di request end ${body}`)

            // Parse form data
            const parsedBody = querystring.parse(body);

            /*
            - Parsebody isinya object, pasangan key value
            - Contoh: parsedBody = { username: 'budi', password: '123' }
            - Jadi, untuk akses value, cukup call key dari variabelnya.
            - const username = parsedBody.username; -> budi
            - const password = parsedBody.password; -> 123
            */

            const username = parsedBody.username || 'tidak diisi';
            const password = parsedBody.password || 'tidak diisi'; 

            console.log(`Login attempt: ${username} : ${password}`);

            // Kasih response
            response.writeHead(200, {"content-type" : 'text/html'});
            response.end(
                `
                <h1>Login diterima!</h1>
                <p>Username: <strong>${username}</strong></p>
                <p>Password: <strong>${password}</strong></p>
                <br>
                <a href="/">Kembali ke halaman utama</a>
                `
            );
        });
    }

    // Homepage dengan form
    else if (method === 'GET' && url === '/') {
        response.writeHead(200, {"content-type":'text/html'});
        response.end(
            `
            <!DOCTYPE html>
            <html>
                <head>
                    <title>
                        Belajar Data Handler
                    </title>

                    <style>
                        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
                        form { margin: 20px 0; padding: 20px; border: 1px solid #ddd; }
                        input, button { padding: 8px; margin: 5px; }
                    </style>
                </head>

                <body>
                    <h1>
                        Data Handler Server
                    </h1>

                    <h2>
                        Test GET Request : Search
                    </h2>

                    <p>
                        <a href="/search?q=javascript&category=backend">
                            Coba: /search?q=javascript&category=backend
                        </a>
                    </p>

                    <h2>
                        Test POST Request : Login Form
                    </h2>

                    <form action="/login" method="POST">
                        <input type="text" name="username" placeholder="Username" required><br>
                        <input type="password" name="password" placeholder="Password" required><br>
                        <button type="submit">Login</button>
                    </form>

                    <h2>
                        Uji Coba Manual
                    </h2>

                    <p>
                        Coba akses: <a href="/search?q=nodejs">
                            /search?q=nodejs
                        </a>
                    </p>
                </body>
            </html>
            `
        );
    }

    // 404 Handler
    else {
        response.writeHead(404, {"content-type":'text/html'});
        response.end(
            `
            <h1>
                404 : Not Found?
            </h1>

            <a href="/">
                Kembali ke halaman utama
            </a>
            `
        );
    }
    ;
});

server.listen(3002, () => {
    console.log('Server running di http://localhost:3002');
    console.log('Test:');
    console.log('1. Buka http://localhost:3002');
    console.log('2. Coba form login');
    console.log('3. Coba akses /search?q=javascript');
})