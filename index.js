const express = require("express");
const app = express();
const mongoose = require("mongoose");
const candidateRoutes=require('./routes/candidate')
const recruiterRoutes=require('./routes/recruiter')
const jwt = require('jsonwebtoken');
const JWT_KEY="thisissecret"
const bodyParser = require("body-parser");



mongoose
  .connect("mongodb://localhost:27017/SquareBoatTask", {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => {
    console.log("DB CONNECTED");
  });



app.use(bodyParser.json());

app.use("/api", candidateRoutes);
app.use("/api", recruiterRoutes);










app.get('/', (req, res)=>{
    res.status(200);
    res.send("Welcome to root URL of Server");
});
const port =  8000;

app.listen(port, (error) =>{
    if(!error)
        console.log("App is listening on port "+ port)
    else 
        console.log("Error occurred, server can't start", error);
    }
);