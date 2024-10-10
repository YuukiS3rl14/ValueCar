const express = require('express');

const app = express();

const bcrypt = require('bcryptjs');

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});