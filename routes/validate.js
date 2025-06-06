const jwt = require('jsonwebtoken');
const JWT_KEY = "thisissecret";

const validate = (req, res, next) => {
    const token = req.headers['access_token'];

    if (!token) {
        return res.status(401).json({ message: 'Access token is missing' });
    }

    jwt.verify(token, JWT_KEY, (err, user) => {
        if (err) {
            return res.status(403).json({ message: 'Invalid token' });
        }

        req.user = user;
        next(); 
    });
};

module.exports = validate;
