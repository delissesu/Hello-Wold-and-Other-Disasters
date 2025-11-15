import { sqlite3 } from './node_modules/sqlite3/lib/sqlite3.d';
import HttpProxyAgent from './node_modules/http-proxy-agent/dist/agent.d';

const http = require('http');
const sqlite3 = require('sqlite3').verbose();
const url = require('url');
const queryString = require('querystring');

// Buat/buka database
const db = new sqlite3.Database('mydatabase.db', (err) => {
    if (err) {
        console.log("Error saat ingin membuka server")
    } else {
        console.log("Berhasil terhubung ke server")

        // Buat tabel user jika belum ada
        db.run(`
            CREATE TABLE IF NOT EXIST users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNQIUE NOT NULL,
            age INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            `);
    }
});

const server = http.createServer(async (request, response) => {
    const { method, url: reqUrl } = request;
    const parsedUrl = url.parse(reqUrl, true);
    const pathname = parsedUrl.pathname;

    // Setting CORS headers
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    response.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    // Handle preflight
    if (method === 'OPTIONS') {
        response.writeHead(200);
        response.end();
        return;
    }
})
