import React from 'react';
import ReactDOMServer from 'react-dom/server';
import HelloWorld from './components/HelloWorld';
import express from 'express';
var bodyParser =  require("body-parser");



var change = "this should change"

let app = express();

// Set the view engine to ejs
app.set('view engine', 'ejs');

// Serve static files from the 'public' folder
app.use(express.static('public'));
app.use(bodyParser.json())

// GET /
app.get('/', function (req, res) {
  res.render('layout', {
    content: ReactDOMServer.renderToString(<HelloWorld />)
  });
});

app.get('/chill', function (req, res) {
  res.send(change)
});


// Start server
let server = app.listen(1337, function () {
  let host = server.address().address;
  let port = server.address().port;

  if (host === '::') {
    host = 'localhost';
  }

  console.log('Example app listening at http://%s:%s', host, port);
});

// POST method route
app.post('/p', function (req, res) {


	console.log("received a request")
	console.log(req)
	console.log(req.body)
	console.log("logged request")
	change = "gang"
  res.send('POST request to the homepage')
})
