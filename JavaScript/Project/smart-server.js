// Import module HTTP (built in di Node JS)
const http = require('http');

// Buat servernya
const server = http.createServer((request, response) => {

    // Get URL yang diminta
    const URL = request.url;
    const METHOD = request.method;

    // Logging
    console.log(`Request => ${METHOD} : ${URL}`);
})