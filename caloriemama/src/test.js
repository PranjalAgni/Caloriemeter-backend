const fs = require('fs');
const FormData = require('form-data');
const fetch = require('node-fetch');
const formData = new FormData();

formData.append(
  'media',
  fs.createReadStream(
    '/Users/pranjal.dev/coding/python-code/Food101Project/apple.jpeg'
  )
);

let url = 'https://www.caloriemama.ai/api/food_recognition_proxy';

let option = {
  method: 'POST',
  headers: {
    'Content-Type': 'multipart/form-data; boundary=---011000010111000001101001',
    Referer: 'https://www.caloriemama.ai/api',
  },
};

options.body = formData;

fetch(url, option)
  .then((res) => res.json())
  .then((json) => console.log(json))
  .catch((err) => console.error('error:' + err));
