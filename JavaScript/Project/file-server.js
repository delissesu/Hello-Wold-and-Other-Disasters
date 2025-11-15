const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    const { url, method } = req;
    
    console.log(`📁 ${method} ${url}`);

    // Handle root path - serve index.html
    if (url === '/' && method === 'GET') {
        serveFile(res, 'public/index.html', 'text/html');
    }
    
    // Handle other file requests
    else if (method === 'GET' && url.startsWith('/')) {
        const filePath = 'public' + url;
        serveFile(res, filePath, getContentType(filePath));
    }
    
    else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 - File Not Found</h1>');
    }
});

// Function untuk serve file
function serveFile(res, filePath, contentType) {
    const fullPath = path.join(__dirname, filePath);
    
    fs.readFile(fullPath, (err, data) => {
        if (err) {
            if (err.code === 'ENOENT') {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.end('<h1>404 - File Not Found</h1>');
            } else {
                res.writeHead(500, { 'Content-Type': 'text/html' });
                res.end('<h1>500 - Server Error</h1>');
            }
            return;
        }
        
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(data);
    });
}

// Function untuk determine content type
function getContentType(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    const contentTypes = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'text/javascript',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.gif': 'image/gif',
        '.json': 'application/json'
    };
    
    return contentTypes[ext] || 'text/plain';
}

// Jalankan server di port 3003
server.listen(3003, () => {
    console.log('📁 File Server running di http://localhost:3003');
    console.log('Test:');
    console.log('1. Buka http://localhost:3003');
    console.log('2. Coba akses file langsung: http://localhost:3003/style.css');
});