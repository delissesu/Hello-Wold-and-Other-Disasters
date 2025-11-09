// Hari 3: "Data Handler" - Processing Request Data & POST Handling

const HTTP = require('http');
const QUERY_STRING = require('querystring');

const SERVER = HTTP.createServer((request, response) => {
    const {
        url,
        method
    } = request;

    console.log(`${method} : ${url}`);
})