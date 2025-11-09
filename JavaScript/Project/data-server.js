// Hari 3: "Data Handler" - Processing Request Data & POST Handling

const http = require('http');
const querystring = require('querystring');
const { URLSearchParams } = require('url');

const server = http.createServer((request, response) => {
    const { url, method } = request;

    console.log(`${method} : ${url}`);

    //Handle GET request : search/query parameter
    if (method === 'GET' && url.includes('/search')) {

        // Ekstrak query parameter dari URL
        const queryString = url.split('?');
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
    };

    
})