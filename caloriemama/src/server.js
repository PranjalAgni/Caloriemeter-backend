const express = require('express');
const cors = require('cors');
const app = express();
const fetch = require('node-fetch');
const multer = require('multer');
const FormData = require('form-data');
const fs = require('fs');
const path = require('path');

const storage = multer.memoryStorage();

const upload = multer({ storage: storage });

const fetchCalories = async (file) => {
  const formData = new FormData();

  formData.append(
    'media',
    fs.createReadStream(
      '/Users/pranjal.dev/coding/python-code/Food101Project/apple.jpeg'
    )
  );

  const response = await fetch(
    'https://www.caloriemama.ai/api/food_recognition_proxy',
    {
      headers: {
        accept: '*/*',
        'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type':
          'multipart/form-data; boundary=----WebKitFormBoundarymnoAHmBcPfb63NvH',
        pragma: 'no-cache',
        'sec-ch-ua':
          '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'x-requested-with': 'XMLHttpRequest',
        cookie: 'ext_name=ojplmecpdpgccookcobabopnaifgidhf',
        Referer: 'https://www.caloriemama.ai/api',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
      },
      body: formData,
      method: 'POST',
    }
  );

  return response;
};

app.use(cors());
// app.use(express.json());

app.post('/calories', upload.single('input'), async (req, res) => {
  console.log('This is the uploaded file ', req.file);
  const response = await fetchCalories(req.file);
  console.log(response);
  const body = await response.text();

  res.json({ calories: 100, body });
});

app.listen(3300, () => {
  console.log(`App running on http://localhost:3300`);
});
